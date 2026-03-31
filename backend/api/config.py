from fastapi import APIRouter, Depends, HTTPException
from supabase import Client
from backend.database import get_supabase
from backend.dependencies import get_current_user
from backend.models.schemas import ConfigResponse, ConfigUpdate
import traceback

router = APIRouter()

@router.get("/", response_model=ConfigResponse)
async def get_config(
    current_user: dict = Depends(get_current_user),
    db: Client = Depends(get_supabase)
):
    """
    Obtiene la configuración actual del usuario autenticado.
    Si no existe fila para él, inicializa una usando los valores por defecto
    y RLS en base de datos.
    """
    user_id = current_user.get("id")
    
    try:
        response = db.table("config").select("*").eq("user_id", user_id).execute()
        
        # Si ya existe, retornarla
        if response.data and len(response.data) > 0:
            return response.data[0]
        
        # Si no existe, crear la fila inicial con default
        default_config = {
            "user_id": user_id, 
            "nombre_usuario": "José Bener", # O "Usuario" genérico
            "meta_financiera": 0.00
        }
        
        insert_response = db.table("config").insert(default_config).execute()
        
        if insert_response.data:
            return insert_response.data[0]
            
        raise HTTPException(status_code=500, detail="Fallo al generar config predeterminada")

    except Exception as e:
        print(f"Error get_config: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="Error interno al consultar la configuración")

@router.put("/", response_model=ConfigResponse)
async def update_config(
    updates: ConfigUpdate,
    current_user: dict = Depends(get_current_user),
    db: Client = Depends(get_supabase)
):
    """
    Actualiza la configuración del usuario autenticado. 
    (Ej: alterar nombre, meta financiera).
    """
    user_id = current_user.get("id")
    update_data = updates.model_dump(exclude_unset=True)
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No se enviaron campos para actualizar")

    try:
        response = db.table("config").update(update_data).eq("user_id", user_id).execute()
        
        if response.data and len(response.data) > 0:
            return response.data[0]
            
        raise HTTPException(status_code=404, detail="Configuración no encontrada para modificar.")

    except Exception as e:
        print(f"Error update_config: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="Error modificando configuración en la base de datos.")
