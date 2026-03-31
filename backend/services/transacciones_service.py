from supabase import Client
from backend.models.schemas import TransaccionCreate, TransaccionUpdate
from typing import Optional, List, Dict, Any
from fastapi import HTTPException
import traceback
import uuid

class TransaccionService:
    def __init__(self, db: Client):
        self.db = db

    def get_all(self, user_id: str, mes: Optional[str] = None, categoria: Optional[str] = None, solo_sunat: Optional[bool] = None) -> List[Dict[str, Any]]:
        try:
            query = self.db.table("transacciones").select("*").eq("user_id", user_id)
            
            # TODO: Implemenar filtros con supabase python (usando ilike, gte, lte, etc.)
            if categoria:
                query = query.eq("categoria", categoria)
                
            if solo_sunat:
                query = query.not_.is_("sunat", "null")
                
            # Filtro por mes (mes debe venir en formato YYYY-MM)
            if mes:
                year, month = mes.split("-")
                start_date = f"{year}-{month}-01"
                # Usamos una fecha límite aproximada para simplificar
                # o podríamos pedir `start_date` y `end_date` desde el endpoint.
                query = query.gte("fecha", start_date).lte("fecha", f"{year}-{month}-31")

            # Ordenar por fecha descendente
            query = query.order("fecha", desc=True)
            
            result = query.execute()
            return result.data
        except Exception as e:
            print(f"Error en get_all transacciones: {traceback.format_exc()}")
            raise HTTPException(status_code=500, detail="Error consultando transacciones")

    def create(self, user_id: str, transaccion: TransaccionCreate) -> Dict[str, Any]:
        data = transaccion.model_dump(mode='json')
        data["user_id"] = user_id
        
        # -----------------------------------------------------
        # REGLA DE NEGOCIO: Binance (Ejemplo de doble registro)
        # Si la categoría es Binance y es una Salida (ej: comprar crypto)
        # podríamos generar un registro de comisión automática.
        # Aquí documentamos una simulación básica de esa lógica:
        # -----------------------------------------------------
        if data.get("categoria", "").lower() == "binance" and data.get("descripcion", "") == "Arbitraje":
            # Aquí podríamos insertar una segunda transacción de "Comisión" 
            # de forma automática. 
            pass

        try:
            result = self.db.table("transacciones").insert(data).execute()
            if result.data:
                return result.data[0]
            raise HTTPException(status_code=500, detail="No se pudo crear la transacción")
        except Exception as e:
            print(f"Error creando transacción: {traceback.format_exc()}")
            raise HTTPException(status_code=500, detail="Error en base de datos al crear transacción")

    def update(self, user_id: str, transaccion_id: str, update_data: TransaccionUpdate) -> Dict[str, Any]:
        data = update_data.model_dump(exclude_unset=True, mode='json')
        if not data:
            raise HTTPException(status_code=400, detail="No hay datos para actualizar")

        try:
            # RLS de Supabase nos protege, pero igual explícitamente obligamos a coincidir user_id
            result = self.db.table("transacciones").update(data)\
                        .eq("id", transaccion_id)\
                        .eq("user_id", user_id)\
                        .execute()
            
            if result.data:
                return result.data[0]
            raise HTTPException(status_code=404, detail="Transacción no encontrada o sin permisos")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error actualizando transacción")

    def delete(self, user_id: str, transaccion_id: str) -> dict:
        try:
            result = self.db.table("transacciones").delete()\
                        .eq("id", transaccion_id)\
                        .eq("user_id", user_id)\
                        .execute()
            
            if result.data:
                return {"status": "success", "message": "Transacción eliminada correctamente"}
            raise HTTPException(status_code=404, detail="Transacción no encontrada")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error eliminando transacción")
