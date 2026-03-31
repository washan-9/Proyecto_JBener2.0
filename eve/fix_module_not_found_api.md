# Registro de Error: ModuleNotFoundError al iniciar Uvicorn

## ¿Cuál fue el error?
Al reiniciar el contenedor e iniciar FastAPI con el comando `uvicorn backend.main:app`, los logs de Docker devolvieron el siguiente error fatal matando el servidor:
`ModuleNotFoundError: No module named 'api'`

## ¿Cuál fue la causa u origen?
El `Dockerfile` establece el directorio de trabajo (`WORKDIR`) en `/app` donde se copia todo el código. Desde allí, el punto de inicio que levanta Docker es ejecutar `backend.main:app`. Por tanto, Python considera `/app` como el root package en `sys.path`. 

Debido a esto, los importes relativos directos dentro de `backend/main.py` o los otros archivos de backend (como `from api.auth import router` o `from database import get_supabase`) fallan, ya que Python busca directamente un paquete llamado `api` o `database` en la raíz `/app`, pero su ubicación real es `/app/backend/api` y `/app/backend/database.py`.

## ¿Cómo se solucionó (código/enfoque)?
Se modificaron todos los archivos del backend donde se hacen importaciones cruzadas entre módulos propios para utilizar rutas absolutas especificando el paquete `backend`.

Ejemplo del cambio implementado:
**Antes:**
```python
from api.auth import router as auth_router
from models.schemas import LoginRequest
```

**Después:**
```python
from backend.api.auth import router as auth_router
from backend.models.schemas import LoginRequest
```
