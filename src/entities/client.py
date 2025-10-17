from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class PerfilEnum(str, Enum):
    conservador = "conservador"
    moderado = "moderado"
    agressivo = "agressivo"

class Cliente(BaseModel):
    """
    Entidade Cliente usando Pydantic
    Representa um cliente no domínio da aplicação
    """
    id: Optional[int] = Field(
        None
    )
    nome: str = Field(
        ...,
        min_length=1,
        max_length=45
    )
    sobrenome: str = Field(
        ...,
        min_length=1,
        max_length=45
    )
    perfil: PerfilEnum = Field(
        ...,
        
    )
    idade: int = Field(
        ...,
        ge=18,
        
    )

    class Config:
        from_attributes = True

    def __str__(self):
        return f"Cliente: {self.nome} {self.sobrenome} ({self.perfil})"

Cliente.model_rebuild()
