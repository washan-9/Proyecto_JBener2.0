from fastapi import APIRouter, Depends, Query, Path
from pydantic import condecimal
from typing import List, Optional
from uuid import UUID

from backend.models.schemas import TransaccionCreate, TransaccionUpdate, TransaccionResponse
from backend.database import get_supabase
from backend.dependencies import get_current_user
from supabase import Client
from backend.services.transacciones_service import TransaccionService

router = APIRouter()

# Dependency para inyectar el servicio de transacciones
def get_transaccion_service(db: Client = Depends(get_supabase)) -> TransaccionService:
    return TransaccionService(db)

@router.get("/", response_model=List[TransaccionResponse])
async def list_transacciones(
    mes: Optional[str] = Query(None, description="Mes en formato YYYY-MM"),
    categoria: Optional[str] = Query(None),
    solo_sunat: Optional[bool] = Query(False),
    current_user: dict = Depends(get_current_user),
    service: TransaccionService = Depends(get_transaccion_service)
):
    """Obtiene la lista de transacciones del usuario, con soporte para filtros."""
    return service.get_all(
        user_id=current_user["id"], 
        mes=mes, 
        categoria=categoria, 
        solo_sunat=solo_sunat
    )

@router.post("/", response_model=TransaccionResponse)
async def create_transaccion(
    transaccion: TransaccionCreate,
    current_user: dict = Depends(get_current_user),
    service: TransaccionService = Depends(get_transaccion_service)
):
    """Crea una nueva transacción."""
    return service.create(user_id=current_user["id"], transaccion=transaccion)

@router.put("/{transaccion_id}", response_model=TransaccionResponse)
async def update_transaccion(
    transaccion_id: UUID = Path(...),
    transaccion_update: TransaccionUpdate = ...,
    current_user: dict = Depends(get_current_user),
    service: TransaccionService = Depends(get_transaccion_service)
):
    """Actualiza parcialmente una transacción existente."""
    return service.update(
        user_id=current_user["id"], 
        transaccion_id=str(transaccion_id), 
        update_data=transaccion_update
    )

@router.delete("/{transaccion_id}")
async def delete_transaccion(
    transaccion_id: UUID = Path(...),
    current_user: dict = Depends(get_current_user),
    service: TransaccionService = Depends(get_transaccion_service)
):
    """Elimina una transacción existente."""
    return service.delete(user_id=current_user["id"], transaccion_id=str(transaccion_id))
