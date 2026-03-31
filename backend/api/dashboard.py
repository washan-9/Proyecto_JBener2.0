from fastapi import APIRouter, Depends, Query, HTTPException
from supabase import Client
from typing import Optional, Dict, Any
from datetime import datetime
from backend.database import get_supabase
from backend.dependencies import get_current_user

router = APIRouter()

@router.get("/summary")
async def get_dashboard_summary(
    mes: Optional[str] = Query(None, description="Mes en formato YYYY-MM. Por defecto mes actual."),
    current_user: dict = Depends(get_current_user),
    db: Client = Depends(get_supabase)
):
    """
    Retorna un resumen consolidado para el dashboard: 
    Total de ingresos, total de gastos, meta actual, progreso, etc.
    """
    user_id = current_user["id"]
    
    if not mes:
        now = datetime.now()
        mes = f"{now.year}-{now.month:02d}"

    year, month = mes.split("-")
    start_date = f"{year}-{month}-01"
    end_date = f"{year}-{month}-31"

    try:
        # Recuperar la meta y configuración
        config_res = db.table("config").select("*").eq("user_id", user_id).execute()
        meta = config_res.data[0]["meta_financiera"] if config_res.data else 0.0

        # Recuperar transacciones del mes
        trans_res = db.table("transacciones").select("*")\
            .eq("user_id", user_id)\
            .gte("fecha", start_date)\
            .lte("fecha", end_date)\
            .execute()
        
        ingresos = 0.0
        gastos = 0.0
        saldo_actual = 0.0 # Opcional: Esto podría requerir sumar todo el histórico, pero simplificaremos al mensual o asumiendo saldo mensual
        
        for t in trans_res.data:
            monto = float(t["monto"])
            if t["tipo"] == "Entrada":
                ingresos += monto
                saldo_actual += monto
            elif t["tipo"] == "Salida":
                gastos += monto
                saldo_actual -= monto
            # "Interno" no afecta ingresos o gastos totales
        
        progreso = min(100, (saldo_actual / meta * 100)) if meta > 0 and saldo_actual > 0 else 0.0

        return {
            "mes": mes,
            "ingresos": ingresos,
            "gastos": gastos,
            "saldo_mes": saldo_actual,
            "meta": meta,
            "progreso_meta_pct": round(progreso, 2)
        }
        
    except Exception as e:
        print(f"Error generando dashboard: {e}")
        raise HTTPException(status_code=500, detail="Error al calcular métricas")
