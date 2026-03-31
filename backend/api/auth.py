from fastapi import APIRouter, HTTPException, Depends
from backend.models.schemas import LoginRequest, Token
from backend.database import get_supabase
from supabase import Client
import traceback

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(credentials: LoginRequest, db: Client = Depends(get_supabase)):
    """
    Inicia sesión contra Supabase Auth y retorna el Access Token (JWT).
    Esto mantendrá nuestra API stateless sin depender de sesiones por cookies.
    """
    try:
        response = db.auth.sign_in_with_password({
            "email": credentials.email,
            "password": credentials.password
        })
        
        session = response.session
        if not session:
            raise HTTPException(status_code=401, detail="Error de autenticación inicial")

        user_data = {
            "id": str(response.user.id),
            "email": response.user.email,
        }

        return Token(
            access_token=session.access_token,
            token_type="bearer",
            user=user_data
        )

    except Exception as e:
        print(f"Error Login: {traceback.format_exc()}")
        raise HTTPException(status_code=401, detail="Credenciales incorrectas o error en el servidor.")

@router.post("/logout")
async def logout(db: Client = Depends(get_supabase)):
    """
    En un entorno stateless (JWT), el logout suele manejarse en el cliente (borrando el token).
    Aun así, podemos llamar a la API de Supabase para revocarlo si es necesario.
    """
    try:
        db.auth.sign_out()
        return {"message": "Sesión cerrada con éxito"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error al cerrar sesión")
