-- ==========================================
-- SCRIPT DE CREACIÓN DE BASE DE DATOS
-- PROYECTO: JBener 2.0
-- ==========================================

-- 1. EXTENSIONES
-- Requerido para generar UUIDs automáticamente
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ==========================================
-- 2. CREACIÓN DE TABLAS
-- ==========================================

-- TABLA: config (Configuraciones de Usuario)
CREATE TABLE public.config (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE UNIQUE,
    nombre_usuario TEXT NOT NULL DEFAULT 'Usuario',
    meta_financiera DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- TABLA: transacciones (Historial Financiero)
CREATE TABLE public.transacciones (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    fecha DATE NOT NULL,
    categoria TEXT NOT NULL,
    monto DECIMAL(12, 2) NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('Entrada', 'Salida', 'Interno')),
    sunat TEXT,
    descripcion TEXT,
    fecha_devolucion DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- ==========================================
-- 3. SEGURIDAD DE FILAS (Row Level Security - RLS)
-- ==========================================

-- Habilitar RLS en ambas tablas
ALTER TABLE public.config ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.transacciones ENABLE ROW LEVEL SECURITY;

-- Políticas para 'config'
-- Los usuarios solo pueden ver y editar su propia configuración
CREATE POLICY "Usuarios pueden ver su propia configuracion" ON public.config
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Usuarios pueden insertar su propia configuracion" ON public.config
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Usuarios pueden actualizar su propia configuracion" ON public.config
    FOR UPDATE USING (auth.uid() = user_id);

-- Políticas para 'transacciones'
-- Los usuarios solo pueden ver, insertar, actualizar y borrar sus propias transacciones
CREATE POLICY "Usuarios pueden ver sus propias transacciones" ON public.transacciones
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Usuarios pueden insertar sus propias transacciones" ON public.transacciones
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Usuarios pueden actualizar sus propias transacciones" ON public.transacciones
    FOR UPDATE USING (auth.uid() = user_id);

CREATE POLICY "Usuarios pueden eliminar sus propias transacciones" ON public.transacciones
    FOR DELETE USING (auth.uid() = user_id);

-- ==========================================
-- 4. TRIGGERS (Opcional - Actualización de fecha)
-- ==========================================

-- Función para actualizar 'updated_at' automáticamente en la tabla config
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = NOW();
   RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_config_modtime
BEFORE UPDATE ON public.config
FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
