# use_cases/cliente/list_clientes/list_clientes_use_case.py
from sqlmodel import Session
from repositories.client_repository import ClienteRepository

class ListClientesUseCase:
    
    def execute(self, session: Session):
        repository = ClienteRepository(session)
        
        clientes = repository.list()
        
        return [
            {
                "id": cliente.id,
                "nome": cliente.nome,
                "sobrenome": cliente.sobrenome,
                "perfil": cliente.perfil.value,
                "idade": cliente.idade
            }
            for cliente in clientes
        ]