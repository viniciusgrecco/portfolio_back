from enum import Enum as PyEnum
from sqlmodel import SQLModel, Field, Enum, Column
from typing import Optional

class Perfil(str, PyEnum):
    conservador = "conservador"
    moderado = "moderado"
    agressivo = "agressivo"

class ClienteModel(SQLModel, table=True):
    __tablename__ = "clientes"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(max_length=45, index=True)
    sobrenome: str = Field(max_length=45, index=True)
    perfil: Perfil = Field(sa_column=Column(Enum(Perfil), nullable=False, index=True))
    idade: int = Field(index=True)

    def __repr__(self):
        return (f"<ClienteModel(id={self.id}, nome='{self.nome}', sobrenome='{self.sobrenome}', "
                f"perfil='{self.perfil.value if self.perfil else None}', idade={self.idade})>")