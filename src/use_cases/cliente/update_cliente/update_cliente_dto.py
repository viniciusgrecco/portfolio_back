# use_cases/cliente/update_cliente/update_cliente_dto.py
from pydantic import BaseModel, Field
from typing import Optional
from entities.client import PerfilEnum

class UpdateClienteDTO(BaseModel):
    """DTO para atualização de cliente"""
    nome: Optional[str] = Field(None, min_length=1, max_length=45, description="Nome do cliente", example="João")
    sobrenome: Optional[str] = Field(None, min_length=1, max_length=45, description="Sobrenome do cliente", example="Silva")
    perfil: Optional[PerfilEnum] = Field(None, description="Perfil de investimento", example="agressivo")
    idade: Optional[int] = Field(None, ge=18, description="Idade do cliente", example=31)

