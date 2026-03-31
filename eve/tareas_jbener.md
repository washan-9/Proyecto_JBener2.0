# Plan de Tareas · Proyecto JBener

Basado en la arquitectura, diseño y requerimientos plasmados en los documentos de definición.
## Metodología de Trabajo y Bucle de Mejora
- **Ramas y Pull Requests**: Desarrollar cada fase o tarea en ramas secundarias (`feat/...`, `chore/...`, `fix/...`) y hacer merge a `main` vía Pull Request.
- **Bucle de Mejora Automática**: Cada vez que se corrija un error en el código, es obligatorio crear un archivo Markdown en esta carpeta (`eve/`) documentando:
  1. ¿Cuál fue el error?
  2. ¿Cuál fue la causa u origen?
  3. ¿Cómo se solucionó (código/enfoque)?
  *(Ejemplo de nombre: `eve/fix_auth_token.md`)*

## Fase 0: Repositorio, Estándares y Docker
- [x] Crear archivos base de exclusión: `.gitignore` y `.dockerignore`.
- [x] Crear archivo `.env.example` para documentar las variables de entorno sin exponer claves reales.
- [x] Crear la estructura de directorios estándar (`backend/`, `frontend/`, `supabase/`).
- [x] Escribir un `README.md` inicial con los pasos de instalación.
- [x] *[Git]* Crear rama secundaria `chore/docker-setup`.
- [x] Crear el archivo `Dockerfile` (basado en Python 3.11+) para empaquetar el backend de FastAPI.
- [x] Crear el archivo `docker-compose.yml` para aislar y ejecutar el servicio sin instalar dependencias locales.
- [x] *[Estandarización]* Configurar un formateador/linter de código para Python (ej. `ruff` o `black`) dentro del workflow.
- [x] Construir y probar la ejecución del contenedor (ej: `docker compose up -d`).
- [x] *[Git]* Hacer **Pull Request** y merge a `main`.

## Fase 1: Entorno y Base de Datos (Supabase)
- [x] *[Git]* Crear rama secundaria `feat/database-setup`.
- [x] Crear el proyecto en Supabase.
- [x] Escribir y ejecutar el script `supabase/schema.sql` para crear las tablas `transacciones` y `config`.
- [x] Configurar las políticas de Row Level Security (RLS) en Supabase para proteger los datos de usuario.
- [x] Crear el usuario administrador (José Bener) en Supabase Auth.
- [x] Migrar el historial de datos desde el archivo CSV actual hacia la nueva base de datos PostgreSQL.
- [x] Configurar el archivo `.env` local (`SUPABASE_URL`, `SUPABASE_KEY`, `SUPABASE_SERVICE_KEY`, `SECRET_KEY`).
- [x] Añadir archivo `.env` al `.gitignore` para evitar filtraciones de seguridad.
- [x] *[Git]* Hacer **Pull Request** y merge a `main`.

## Fase 2: Backend (Python + FastAPI)
- [x] *[Git]* Crear rama secundaria `feat/backend-api`.
- [x] Configurar el punto de entrada `main.py` y probar la ejecución dentro del contenedor (vía `docker-compose.yml`).
- [x] Implementar módulo de conexión a la BD en `backend/database.py` usando `supabase-py`.
- [x] Definir todos los modelos de validación en `backend/models/schemas.py` usando Pydantic v2.
- [x] Desarrollar lógica y endpoint de **Auth** (`api/auth/login`, `api/auth/logout`) con emisión de JWT.
- [x] Desarrollar lógica y endpoints de **Configuración** (`api/config`) para lectura y modificación del nombre y meta.
- [x] Desarrollar servicio de **Transacciones** (`transacciones_service.py`), incluyendo reglas de negocio especiales (ej: dobles registros para Binance).
- [x] Desarrollar endpoints CRUD de **Transacciones** con parámetros de filtro (mes, categoría, solo_sunat).
- [x] Implementar endpoint específico para el cálculo de métricas financieras para el Dashboard.
- [x] Probar y validar todos los endpoints vía Swagger UI (`/docs`).
- [x] *[Git]* Hacer **Pull Request** y merge a `main`.

## Fase 3: Frontend - Sistema de Diseño y Estructura
- [ ] *[Git]* Crear rama secundaria `feat/frontend-ui`.
- [x] Crear estructura base de archivos (`index.html`, `styles.css`, `app.js`, `api.js`).
- [x] Configurar las familias de fuentes: Google Fonts Syne (títulos), Inter (body) y DM Mono (datos numéricos).
- [x] Trasladar los "Tokens CSS" definidos en el Design System a `:root` en `styles.css` (Colores, Espaciados, Radios).
- [x] Configurar clases de tipografías (ej. `display-xl`, `data-md`, `label-sm`).
- [x] Estilar componentes base: Botones (Primary, Outline, Ghost, Gradient CTA).
- [x] Estilar Cards de Activos, Sparklines (con Chart.js) y Badges (positivos/negativos, estado).
- [x] Implementar layout principal: Topbar fijo y Sidebar de navegación.
- [x] Implementar animaciones clave (`fadeUp`, transiciones de hover, y carga).
- [x] Asegurar reglas de responsividad (Plegado de Sidebar en móviles, Bottom sheets).
- [x] *[Git]* Hacer **Pull Request** y merge a `main`.

## Fase 4: Frontend - Lógica, Funcionalidad y Vistas
- [ ] *[Git]* Crear rama secundaria `feat/frontend-logic`.
- [ ] Implementar módulo de conexión `api.js` centralizando `fetch`, envío de token JWT y manejo de expiración (HTTP 401).
- [ ] **Módulo Login:** Desarrollar la vista y flujo de autenticación, guardando la sesión en `localStorage`.
- [ ] **Módulo Dashboard:**
  - [ ] Conectar y mostrar métricas principales con animación "count-up".
  - [ ] Implementar barra de progreso hacia la meta financiera.
  - [ ] Integrar Chart.js para "Evolución Patrimonial" (líneas duales) y distribución de ingresos (dona), configurando filtros de tiempo.
  - [ ] Cargar lista de últimos 6 movimientos y estado del panel de "Por Recuperar".
- [ ] **Registro de movimientos:**
  - [ ] Crear formulario interactivo con campos dinámicos por tipo (fecha de devolución para préstamos, comisión para Binance).
  - [ ] Añadir sección visual con estimación del impuesto a aplicar al seleccionar la categoría.
- [ ] **Módulo de Historial:** Vista con listado, capacidad de filtrado combinado, y botones de eliminación.
- [ ] **Módulo SUNAT:** Cargar resumen con distinción entre renta de 5ta y 2da categoría con cálculo de estimación total.
- [ ] **Módulo Ajustes:** Formulario conectado al endpoint de configuración para modificar la meta económica.
- [ ] *[Git]* Hacer **Pull Request** y merge a `main`.

## Fase 5: Despliegue
- [ ] Hacer *commit* y *push* de código al repositorio GitHub.
- [ ] Configurar el proyecto en Render o Railway, ligándolo al repositorio.
- [ ] Parametrizar las variables de entorno (`.env`) en el panel de control del cloud provider.
- [ ] Validar carga, conexión a Supabase de producción, SSL y performance general.

## Fase 6: Mejoras Futuras (Backlog)
- [ ] Implementar alertas automáticas previas a la fecha de vencimiento de los préstamos.
- [ ] Agregar exportación del resumen SUNAT a un archivo PDF.
- [ ] Integrar API pública para consultas de precios en vivo (ej. cotización real de BTC/USDT).
- [ ] Crear panel analítico de gráficas mensuales (ingresos vs gastos, tracking anual).
- [ ] Habilitar PWA para poder instalar la app web como nativa en el celular.
- [ ] Expandir la arquitectura para soportar multi-usuarios.
