"""
Punto de entrada principal de la API JBener.
Configura la app FastAPI, CORS, variables de entorno y routers.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict


# ---------------------------------------------------------------------------
# Configuración de variables de entorno
# ---------------------------------------------------------------------------

class Settings(BaseSettings):
    """Lee las variables del archivo .env de forma segura."""
    supabase_url: str = ""
    supabase_key: str = ""
    supabase_service_key: str = ""
    secret_key: str = "changeme"

    model_config = SettingsConfigDict(env_file="/app/.env", extra="ignore")


settings = Settings()


# ---------------------------------------------------------------------------
# Instancia de la aplicación
# ---------------------------------------------------------------------------

app = FastAPI(
    title="JBener API",
    description="API del dashboard financiero personal de JBener 2.0",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


# ---------------------------------------------------------------------------
# Middleware CORS
# ---------------------------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # En producción limitar al dominio del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Routers (se irán montando a medida que se creen los módulos)
# ---------------------------------------------------------------------------

from backend.api.auth import router as auth_router
from backend.api.config import router as config_router
from backend.api.transacciones import router as transacciones_router
from backend.api.dashboard import router as dashboard_router

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(config_router, prefix="/api/config", tags=["Config"])
app.include_router(transacciones_router, prefix="/api/transacciones", tags=["Transacciones"])
app.include_router(dashboard_router, prefix="/api/dashboard", tags=["Dashboard"])


# ---------------------------------------------------------------------------
# Endpoints base
# ---------------------------------------------------------------------------

@app.get("/", tags=["Root"])
def root():
    """Endpoint raíz — confirma que la API está en línea."""
    return {"status": "ok", "message": "JBener API corriendo correctamente."}


@app.get("/health", tags=["Health"])
def health_check():
    """Endpoint de salud para monitoreo y Docker healthcheck."""
    return {"status": "healthy", "version": app.version}
