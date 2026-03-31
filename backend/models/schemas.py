from pydantic import BaseModel, Field, condecimal
from typing import Optional
from datetime import date, datetime
from uuid import UUID

# ==========================================
# ESQUEMAS PARA CONFIGURACIÓN
# ==========================================

class ConfigBase(BaseModel):
    nombre_usuario: str = Field(..., example="Usuario")
    meta_financiera: condecimal(max_digits=12, decimal_places=2) = Field(0.00, example=15000.50)

class ConfigUpdate(BaseModel):
    nombre_usuario: Optional[str] = None
    meta_financiera: Optional[condecimal(max_digits=12, decimal_places=2)] = None

class ConfigResponse(ConfigBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ==========================================
# ESQUEMAS PARA TRANSACCIONES
# ==========================================

class TransaccionBase(BaseModel):
    fecha: date = Field(..., example="2023-10-15")
    categoria: str = Field(..., example="Alimentación")
    monto: condecimal(max_digits=12, decimal_places=2) = Field(..., example=50.00)
    tipo: str = Field(..., pattern="^(Entrada|Salida|Interno)$", example="Salida")
    sunat: Optional[str] = Field(None, example="5ta Categoría")
    descripcion: Optional[str] = Field(None, example="Almuerzo en restaurante")
    fecha_devolucion: Optional[date] = Field(None, example="2023-11-15")

class TransaccionCreate(TransaccionBase):
    pass

class TransaccionUpdate(BaseModel):
    fecha: Optional[date] = None
    categoria: Optional[str] = None
    monto: Optional[condecimal(max_digits=12, decimal_places=2)] = None
    tipo: Optional[str] = Field(None, pattern="^(Entrada|Salida|Interno)$")
    sunat: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_devolucion: Optional[date] = None

class TransaccionResponse(TransaccionBase):
    id: UUID
    user_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


# ==========================================
# ESQUEMAS PARA AUTENTICACIÓN
# ==========================================

class LoginRequest(BaseModel):
    email: str = Field(..., example="jose@bener.com")
    password: str = Field(..., example="supersecreto123")

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict  # Retornaremos la info básica del usuario aquí para el frontend
