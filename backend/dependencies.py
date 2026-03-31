from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import Client
from backend.database import get_supabase
import traceback
import jwt
import os

# Utilizamos el esquema Bearer para leer el token de las cabeceras HTTP
security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Client = Depends(get_supabase)
):
    """
    Lee y valida el token JWT del header 'Authorization: Bearer <token>'.
    Retorna la información del usuario en caso de ser válido.
    """
    token = credentials.credentials
    jwt_secret = os.environ.get("SUPABASE_JWT_SECRET")

    if not jwt_secret:
        # Fallback de seguridad si usamos localmente:
        raise HTTPException(
            status_code=500, 
            detail="Falta configurar SUPABASE_JWT_SECRET en el entorno"
        )
    
    try:
        # Validar configuración JWT (aud, algoritmo usado por Supabase)
        # Supabase por defecto usa HS256 y la audiencia es 'authenticated' o la default
        payload = jwt.decode(
            token, 
            jwt_secret, 
            algorithms=["HS256"], 
            options={"verify_aud": False} # Deshabilitamos temporalmente aud para simplificar si no definen una estricta
        )
        
        # El sub (Subject) en el JWT de Supabase es el UUID del usuario
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Token inválido: falta 'sub'")

        # Podríamos hacer db.auth.get_user(token) alternativamente, pero decodificarlo localmente
        # es mucho más rápido y evita ping-pong de red (Stateless puro)
        
        return {"id": user_id, "email": payload.get("email")}

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="El token ha expirado. Inicie sesión nuevamente.")
    except jwt.JWTError as e:
        print(f"Error decodificando JWT: {e}")
        raise HTTPException(status_code=401, detail="No se pudo validar las credenciales (Token inválido).")
    except Exception as e:
        print(f"Error get_current_user: {traceback.format_exc()}")
        raise HTTPException(status_code=401, detail="Acceso denegado")
