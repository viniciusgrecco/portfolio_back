from pydantic import BaseModel, Field
from entities.client import PerfilEnum

class CreateClienteDTO(BaseModel):
    """DTO para criação de cliente"""
    nome: str = Field(..., min_length=1, max_length=45, description="Nome do cliente", example="João")
    sobrenome: str = Field(..., min_length=1, max_length=45, description="Sobrenome do cliente", example="Silva")
    perfil: PerfilEnum = Field(..., description="Perfil de investimento", example="moderado")
    idade: int = Field(..., ge=18, description="Idade do cliente (mínimo 18 anos)", example=30)
