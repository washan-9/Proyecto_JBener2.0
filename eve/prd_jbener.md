# JBener · Product Requirements Document

**Versión:** 1.0  
**Autor:** José Bener  
**Fecha:** Marzo 2026  
**Estado:** Activo

---

## 1. Resumen Ejecutivo

JBener es una aplicación web personal de gestión financiera diseñada para que José Bener pueda monitorear, registrar y analizar sus activos, movimientos de caja, inversiones en criptomonedas y obligaciones tributarias en Perú, con el objetivo de alcanzar una meta de libertad financiera de S/. 50,000.

> **Problema central:** El usuario gestiona sus finanzas en archivos CSV locales sin respaldo, sin acceso remoto, sin autenticación real y sin visualización clara del progreso hacia la meta. Esto genera riesgo de pérdida de datos y dificulta la toma de decisiones financieras informadas.

> **Solución propuesta:** Aplicación web moderna con backend FastAPI, base de datos PostgreSQL en Supabase y frontend HTML/JS con dashboard interactivo. Accesible desde cualquier dispositivo, con autenticación segura, gráficos en tiempo real y módulo de cumplimiento SUNAT integrado.

---

## 2. Contexto y Objetivos

### 2.1 Contexto del proyecto

El proyecto surge de la necesidad de José Bener de tener visibilidad clara y en tiempo real sobre su situación financiera personal. Actualmente maneja su información en archivos CSV que solo funcionan en su computadora local, con una interfaz Streamlit básica que no permite acceso móvil ni tiene autenticación real.

El usuario tiene múltiples fuentes de ingreso (sueldos, intereses, criptomonedas), realiza préstamos a terceros y necesita llevar control de sus obligaciones con SUNAT como contribuyente peruano.

### 2.2 Objetivo principal

Proveer una herramienta confiable, accesible desde cualquier dispositivo, que permita a José gestionar su camino hacia la libertad financiera de S/. 50,000 con datos reales y seguros.

### 2.3 Objetivos específicos

- Reemplazar los archivos CSV por una base de datos PostgreSQL en la nube con respaldo automático.
- Implementar autenticación real mediante Supabase Auth con sesiones seguras.
- Permitir acceso desde celular y PC mediante una aplicación web responsiva.
- Visualizar en tiempo real el progreso hacia la meta financiera con gráficos interactivos.
- Automatizar el cálculo de obligaciones tributarias (SUNAT) por tipo de ingreso.
- Registrar y controlar préstamos activos con fechas de devolución y alertas.

---

## 3. Usuarios y Casos de Uso

### 3.1 Perfil de usuario

| Atributo | Descripción |
|---|---|
| Usuario primario | José Bener — único usuario de la aplicación |
| Ubicación | Lima, Perú |
| Dispositivos | PC (trabajo/casa) y celular (consultas rápidas) |
| Nivel técnico | Intermedio — sabe Python básico, usa Streamlit |
| Frecuencia de uso | Diaria para consultas, semanal para registro de movimientos |
| Meta financiera | Acumular S/. 50,000 en patrimonio neto |

### 3.2 Casos de uso principales

#### CU-01 · Registrar un movimiento financiero
El usuario ingresa un nuevo movimiento (sueldo, gasto, préstamo, cripto) con fecha, descripción y monto. El sistema calcula automáticamente el tipo contable, el impacto en el patrimonio y la tasa SUNAT aplicable según la categoría seleccionada.

#### CU-02 · Consultar el dashboard de inicio
El usuario ve en tiempo real: saldo disponible, monto por recuperar de préstamos, valor de criptomonedas, patrimonio total y porcentaje de progreso hacia la meta. Los datos se animan al cargar para facilitar la lectura rápida.

#### CU-03 · Analizar la evolución patrimonial
El usuario filtra el gráfico de líneas por periodo (7D, 30D, 6M, Todo) para ver la evolución de su saldo disponible y patrimonio total a lo largo del tiempo. Puede identificar picos de ingresos y momentos de alto gasto.

#### CU-04 · Gestionar el historial de movimientos
El usuario filtra el historial por mes, categoría o solo declarables SUNAT. Puede eliminar movimientos erróneos. El sistema muestra el monto neto del filtro aplicado.

#### CU-05 · Consultar resumen SUNAT
El usuario ve todos los movimientos con obligación tributaria, el impuesto estimado por cada uno y el total anual a declarar. El sistema diferencia entre renta de quinta categoría (sueldos), segunda categoría (intereses y cripto) y operaciones sin obligación.

#### CU-06 · Registrar operaciones con Binance
Al registrar una compra en Binance, el sistema crea automáticamente dos registros: el traslado del capital como activo cripto y la comisión como gasto fijo. Al registrar una venta, calcula la ganancia neta y registra solo esa ganancia con su tasa SUNAT del 5%.

#### CU-07 · Configurar la meta y nombre del proyecto
El usuario puede cambiar el nombre del proyecto y la meta de inversión desde la sección de Ajustes. El cambio se refleja inmediatamente en el dashboard y en la barra de progreso.

---

## 4. Arquitectura del Sistema

### 4.1 Stack tecnológico

| Capa | Tecnología | Justificación |
|---|---|---|
| Backend API | FastAPI (Python) | Alto rendimiento, tipado con Pydantic, documentación automática con Swagger |
| Base de datos | Supabase (PostgreSQL) | Gratis para proyectos personales, acceso en la nube, Auth integrado, Row Level Security |
| Autenticación | Supabase Auth | JWT seguros, sesiones persistentes, sin implementación manual de hashes |
| Frontend | HTML + CSS + JS vanilla | Sin frameworks innecesarios, carga rápida, compatible con cualquier navegador |
| Gráficos | Chart.js | Liviano, sin dependencias, ideal para dashboards financieros |
| Deploy | Render / Railway | Deploy gratuito conectado a GitHub con CI/CD automático |

### 4.2 Estructura de carpetas

```
jbener/
├── main.py                          # Punto de entrada FastAPI
├── requirements.txt                 # Dependencias Python
├── .env                             # Variables de entorno (no subir a Git)
├── backend/
│   ├── config.py                    # Configuración global con pydantic-settings
│   ├── database.py                  # Conexión a Supabase
│   ├── models/
│   │   └── schemas.py               # Modelos Pydantic (validación de datos)
│   ├── routers/
│   │   ├── auth.py                  # Endpoints /api/auth
│   │   ├── transacciones.py         # Endpoints /api/transacciones
│   │   └── config.py                # Endpoints /api/config
│   └── services/
│       ├── auth_service.py          # Lógica de autenticación
│       ├── transacciones_service.py # Lógica de negocio
│       └── config_service.py        # Lógica de configuración
├── frontend/
│   ├── templates/index.html         # SPA principal
│   └── static/
│       ├── css/styles.css           # Todos los estilos
│       └── js/
│           ├── api.js               # Capa de comunicación con el backend
│           └── app.js               # Lógica del frontend
└── supabase/
    └── schema.sql                   # SQL para crear las tablas
```

### 4.3 Modelo de datos

| Tabla | Campos principales | Descripción |
|---|---|---|
| `transacciones` | id, fecha, categoria, descripcion, monto, tipo, sunat, fecha_devolucion, created_at | Registro principal de todos los movimientos financieros |
| `config` | id, nombre, meta | Configuración del proyecto (una sola fila, id=1) |

#### Tipos de movimiento (campo `tipo`)

| Tipo | Descripción | Impacto en saldo | Impacto en patrimonio |
|---|---|---|---|
| `Entrada` | Ingreso de dinero (sueldo, intereses, ganancias) | + suma | + suma |
| `Salida` | Gasto o egreso de caja | − resta | − resta |
| `Prestado` | Dinero prestado a terceros (activo financiero) | − resta | no cambia |
| `Interno` | Traslado entre cuentas propias (Binance) | no cambia | no cambia |

---

## 5. Funcionalidades del Producto

### 5.1 Módulo Dashboard (Inicio)

- 5 tarjetas de métricas con animación de conteo al cargar: Saldo Disponible, Por Recuperar, Saldo Cripto, Patrimonio Total, Progreso de Meta.
- Barra de progreso animada hacia la meta configurable.
- Gráfico de líneas dual (Saldo disponible vs Patrimonio total) con filtro por periodo.
- Gráfico de dona con distribución de ingresos por categoría.
- Panel de 6 movimientos recientes con ícono, categoría, fecha y monto coloreado.

### 5.2 Módulo de Administración

- Formulario de registro con 7 categorías: Sueldo, Cripto, Gasto Fijo, Préstamo, Interés, Binance (Compra), Binance (Venta).
- Info box contextual que muestra tipo tributario, impuesto estimado e impacto financiero al seleccionar una categoría.
- Campos dinámicos: comisión aparece solo para Binance; fecha de devolución solo para Préstamos.
- Lógica de doble registro automático para operaciones Binance (traslado + comisión).
- Historial con filtros combinables: mes, categoría, solo declarables SUNAT.
- Eliminación de movimientos con confirmación.

### 5.3 Módulo SUNAT

- Vista filtrada de solo los movimientos con obligación tributaria.
- Cálculo automático del impuesto estimado por movimiento según la tasa de su categoría.
- Resumen consolidado: total de ingresos declarables, impuesto total estimado, cantidad de movimientos.
- Diferenciación visual entre 5ta categoría (sueldos) y 2da categoría (intereses/cripto).

### 5.4 Módulo de Ajustes

- Edición del nombre del proyecto (se refleja en el header del dashboard).
- Edición de la meta de inversión en soles (actualiza la barra de progreso en tiempo real).

### 5.5 Autenticación

- Login con email y contraseña via Supabase Auth.
- Token JWT almacenado en localStorage con expiración de 24 horas.
- Redirección automática al login si el token expira o es inválido.
- Botón de cierre de sesión que invalida el token en Supabase.

---

## 6. API Endpoints

| Método | Endpoint | Descripción | Auth |
|---|---|---|---|
| `POST` | `/api/auth/login` | Autenticación con email y contraseña | No |
| `POST` | `/api/auth/logout` | Cierre de sesión | Sí |
| `GET` | `/api/transacciones/` | Listar movimientos (filtros opcionales) | Sí |
| `POST` | `/api/transacciones/` | Registrar uno o más movimientos | Sí |
| `DELETE` | `/api/transacciones/{id}` | Eliminar un movimiento por ID | Sí |
| `GET` | `/api/transacciones/metricas` | Calcular las 5 métricas del dashboard | Sí |
| `GET` | `/api/config/` | Obtener nombre y meta del proyecto | Sí |
| `PUT` | `/api/config/` | Actualizar nombre y meta del proyecto | Sí |

### 6.1 Parámetros de filtro — `GET /api/transacciones/`

| Parámetro | Tipo | Descripción |
|---|---|---|
| `mes` | int (1-12) | Filtra por mes del año en curso |
| `categoria` | string | Filtra por categoría exacta (ej: `Sueldo`) |
| `solo_sunat` | bool | Si es `true`, devuelve solo movimientos con campo `sunat` no vacío |

---

## 7. Reglas de Negocio

### 7.1 Cálculo de métricas

```
Saldo Disponible  = sum(Entradas) - sum(Salidas) - sum(Prestados)
Por Recuperar     = sum(Prestados activos)
Saldo Cripto      = sum(monto donde categoria='Cripto' y tipo != 'Salida')
Patrimonio Total  = Saldo Disponible + Por Recuperar
Progreso Meta     = (Patrimonio Total / Meta) * 100   [máx 100%]
```

### 7.2 Lógica por categoría

| Categoría | Tipo generado | Tasa SUNAT | Registros creados |
|---|---|---|---|
| Sueldo | `Entrada` | 8%-30% | 1 registro |
| Cripto | `Entrada` | — | 1 registro |
| Gasto Fijo | `Salida` | — | 1 registro |
| Préstamo | `Prestado` | — | 1 registro (con fecha devolución) |
| Interés | `Entrada` | 5% | 1 registro |
| Binance (Compra) | `Interno` | — | 2 registros: traslado cripto + comisión como gasto |
| Binance (Venta) | `Entrada` | 5% | 2 registros: ganancia neta + comisión como gasto |

---

## 8. Seguridad

### 8.1 Autenticación y sesiones

- Supabase Auth maneja el hash de contraseñas (bcrypt) sin implementación manual.
- Los tokens JWT tienen expiración de 24 horas.
- El frontend detecta tokens expirados (HTTP 401) y redirige al login sin exponer datos.
- El archivo `.env` nunca debe subirse a Git — agregar al `.gitignore`.

### 8.2 Row Level Security (RLS)

Supabase tiene habilitado RLS en ambas tablas. La política permite acceso solo a usuarios con `auth.role() = 'authenticated'`. Esto significa que incluso si alguien obtuviera la URL de la API, no podría leer ni escribir datos sin un token válido.

### 8.3 Variables de entorno

| Variable | Descripción | Dónde obtenerla |
|---|---|---|
| `SUPABASE_URL` | URL del proyecto Supabase | Supabase → Settings → API → Project URL |
| `SUPABASE_KEY` | Clave anónima (pública) | Supabase → Settings → API → anon key |
| `SUPABASE_SERVICE_KEY` | Clave de servicio (privada) | Supabase → Settings → API → service_role key |
| `SECRET_KEY` | Clave para firmar JWT propios | `python -c "import secrets; print(secrets.token_hex(32))"` |

---

## 9. Plan de Implementación

| Fase | Tareas | Duración estimada |
|---|---|---|
| **Fase 1 — Base de datos** | Crear proyecto en Supabase, ejecutar `schema.sql`, crear usuario en Supabase Auth, migrar datos del CSV existente. | 1 día |
| **Fase 2 — Backend** | Configurar `.env`, instalar dependencias, levantar FastAPI localmente, verificar endpoints con Swagger en `/docs`. | 1 día |
| **Fase 3 — Frontend** | Abrir la app en el navegador, verificar login, dashboard, registro de movimientos y filtros del historial. | 1 día |
| **Fase 4 — Deploy** | Subir el proyecto a GitHub, conectar con Render o Railway, configurar variables de entorno en el panel del hosting. | 1 día |
| **Fase 5 — Mejoras futuras** | Notificaciones de préstamos por vencer, exportación PDF del resumen SUNAT, gráfico de distribución mensual. | Iterativo |

---

## 10. Criterios de Éxito

### 10.1 Funcionales

1. El usuario puede iniciar sesión con email y contraseña y la sesión persiste al cerrar el navegador.
2. Las 5 métricas del dashboard se calculan correctamente a partir de los datos reales en Supabase.
3. El registro de un movimiento Binance (Compra) genera automáticamente 2 registros en la base de datos.
4. El módulo SUNAT muestra solo los movimientos declarables con su impuesto estimado correcto.
5. La aplicación carga y funciona correctamente desde el celular.

### 10.2 No funcionales

1. El tiempo de carga inicial del dashboard es menor a 2 segundos en una conexión normal.
2. Los datos sobreviven un reinicio del servidor (almacenamiento en Supabase, no en memoria).
3. El archivo `.env` no está incluido en el repositorio de GitHub.
4. La URL de la app en producción usa HTTPS.

---

## 11. Mejoras Futuras (Backlog)

| Funcionalidad | Descripción | Prioridad |
|---|---|---|
| Alertas de préstamos | Notificación cuando un préstamo está próximo a vencer (3 días antes de `fecha_devolucion`). | Alta |
| Exportación SUNAT a PDF | Generar un PDF del resumen tributario anual listo para llevar al contador. | Alta |
| Integración precio cripto | Consultar el precio actual de BTC/USDT via API de Binance para mostrar el valor real del portfolio. | Media |
| Gráfico mensual comparativo | Barras que comparen ingresos vs gastos mes a mes durante el año. | Media |
| Modo multi-usuario | Permitir que otros miembros de la familia tengan su propia cuenta con datos separados. | Baja |
| App móvil (PWA) | Convertir el frontend en una Progressive Web App instalable en el celular. | Baja |

---

## 12. Glosario

| Término | Definición |
|---|---|
| **Saldo Disponible** | Dinero efectivamente en mano: ingresos menos gastos y préstamos activos. |
| **Patrimonio Total** | Saldo disponible más el dinero prestado a terceros (que aún es un activo). |
| **Prestado** | Tipo de movimiento donde el dinero sale del saldo pero permanece en el patrimonio como cuenta por cobrar. |
| **Interno** | Traslado entre cuentas propias (ej: banco a Binance) que no afecta ni saldo ni patrimonio. |
| **RLS** | Row Level Security — política de Supabase que restringe el acceso a filas por usuario autenticado. |
| **JWT** | JSON Web Token — token cifrado que identifica al usuario autenticado en cada petición a la API. |
| **SUNAT** | Superintendencia Nacional de Aduanas y de Administración Tributaria — ente recaudador de impuestos en Perú. |
| **5ta Categoría** | Renta de quinta categoría: ingresos por relación de dependencia (sueldos). Tasa: 8% a 30% escalonado. |
| **2da Categoría** | Renta de segunda categoría: intereses, dividendos, ganancias por venta de valores (cripto). Tasa: 5%. |
| **SPA** | Single Page Application — aplicación web que carga una sola vez y actualiza el contenido sin recargar la página. |
| **FastAPI** | Framework Python de alto rendimiento para construir APIs REST con tipado estático y documentación automática. |
| **Supabase** | Plataforma Backend-as-a-Service basada en PostgreSQL con autenticación, storage y API REST integrados. |

---

*PRD v1.0 · JBener · Marzo 2026*
