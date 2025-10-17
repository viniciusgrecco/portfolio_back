from sqlmodel import Session, select
from typing import List, Optional
from models.client_model import ClienteModel, Perfil
from repositories.base_repository import BaseRepository

class ClienteRepository(BaseRepository[ClienteModel]):
    def __init__(self, session: Session):
        super().__init__(session, ClienteModel)

    def get_by_fullname(self, nome: str, sobrenome: str) -> Optional[ClienteModel]:
        """Busca cliente por nome e sobrenome exatos"""
        statement = select(ClienteModel).where(
            ClienteModel.nome == nome,
            ClienteModel.sobrenome == sobrenome
        )
        result = self.session.exec(statement)
        return result.first()

    def get_by_perfil(self, perfil: Perfil) -> List[ClienteModel]:
        """Retorna lista de clientes por perfil (conservador/moderado/agressivo)"""
        statement = select(ClienteModel).where(ClienteModel.perfil == perfil)
        results = self.session.exec(statement)
        return results.all()

    def get_by_nome_partial(self, nome_fragment: str) -> List[ClienteModel]:
        """Busca clientes onde o nome contenha o fragmento (case-insensitive)"""
        statement = select(ClienteModel).where(ClienteModel.nome.contains(nome_fragment))
        results = self.session.exec(statement)
        return results.all()