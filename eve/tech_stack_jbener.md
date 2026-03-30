# Tech Stack · JBener

---

## Backend

| Tecnología | Versión | Para qué se usa |
|---|---|---|
| **Python** | 3.11+ | Lenguaje base de todo el backend |
| **FastAPI** | 0.111.0 | Framework principal de la API REST. Maneja los endpoints `/api/auth`, `/api/transacciones` y `/api/config` |
| **Uvicorn** | 0.29.0 | Servidor ASGI que corre FastAPI en local y producción |
| **Pydantic v2** | 2.7.1 | Validación y serialización de todos los datos de entrada y salida (request/response models) |
| **pydantic-settings** | 2.2.1 | Carga tipada de variables de entorno desde el archivo `.env` |
| **supabase-py** | 2.4.6 | Cliente oficial de Supabase para Python. Queries a la BD y autenticación de usuarios |
| **python-jose** | 3.3.0 | Verificación de tokens JWT emitidos por Supabase Auth |
| **python-multipart** | 0.0.9 | Soporte para formularios en FastAPI |
| **python-dotenv** | 1.0.1 | Lectura del archivo `.env` en entorno local |
| **httpx** | 0.27.0 | Cliente HTTP async, usado internamente por supabase-py |

---

## Base de datos

| Tecnología | Para qué se usa |
|---|---|
| **Supabase** | Plataforma principal. Provee PostgreSQL gestionado en la nube, Auth, Row Level Security y API REST automática |
| **PostgreSQL** | Motor de base de datos. Almacena las tablas `transacciones` y `config` |
| **Row Level Security (RLS)** | Política de seguridad a nivel de fila: solo usuarios autenticados pueden leer y escribir sus datos |

---

## Autenticación

| Tecnología | Para qué se usa |
|---|---|
| **Supabase Auth** | Gestión completa de usuarios: registro, login, hash de contraseñas (bcrypt) y emisión de JWT |
| **JWT (JSON Web Token)** | Token de sesión que el frontend guarda en `localStorage` y envía en cada request al backend como `Authorization: Bearer` |

---

## Frontend

| Tecnología | Para qué se usa |
|---|---|
| **HTML5** | Estructura de la SPA (`index.html`). FastAPI lo sirve como archivo estático para todas las rutas |
| **CSS3 (vanilla)** | Todos los estilos del dashboard: dark theme, tokens CSS, animaciones, responsive |
| **JavaScript (ES Modules)** | Lógica del frontend dividida en `api.js` (comunicación con el backend) y `app.js` (UI, eventos, renders) |
| **Chart.js 4.4** | Gráfico de líneas dual (saldo vs patrimonio) y gráfico de dona de distribución por categoría |
| **Google Fonts** | Fuentes: `Syne` (títulos), `DM Mono` (números y datos financieros) |

---

## Deploy e Infraestructura

| Tecnología | Para qué se usa |
|---|---|
| **GitHub** | Repositorio del código fuente. Base para el CI/CD automático |
| **Render / Railway** | Hosting gratuito del backend FastAPI. Se conecta al repo de GitHub y hace deploy automático en cada push |
| **Supabase (cloud)** | Hosting de la base de datos PostgreSQL. Plan gratuito suficiente para uso personal |

---

## Herramientas de desarrollo

| Herramienta | Para qué se usa |
|---|---|
| **`.env`** | Variables de entorno locales (URLs y claves de Supabase, SECRET_KEY). Nunca se sube a Git |
| **`.gitignore`** | Excluye `.env`, `__pycache__`, `venv/` y archivos temporales del repositorio |
| **Swagger UI** (`/docs`) | Documentación interactiva auto-generada por FastAPI para probar los endpoints durante el desarrollo |
| **Supabase SQL Editor** | Interfaz web para ejecutar el `schema.sql` y gestionar las tablas directamente |

---

## Resumen visual

```
Celular / PC
     │
     ▼
HTML + CSS + JS (frontend)
     │  fetch() con JWT
     ▼
FastAPI + Python (backend)  ←─── .env (claves)
     │  supabase-py
     ▼
Supabase (PostgreSQL + Auth)
```

---

*Tech Stack v1.0 · JBener · Marzo 2026*
