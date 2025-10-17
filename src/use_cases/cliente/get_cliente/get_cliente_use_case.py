# use_cases/cliente/get_cliente/get_cliente_use_case.py
from fastapi import HTTPException
from sqlmodel import Session
from repositories.client_repository import ClienteRepository

class GetClienteUseCase:
    
    def execute(self, cliente_id: int, session: Session):
        repository = ClienteRepository(session)
        
        cliente = repository.get(cliente_id)
        
        if not cliente:
            raise HTTPException(
                status_code=404,
                detail=f"Cliente com ID {cliente_id} não encontrado"
            )
        
        return {
            "id": cliente.id,
            "nome": cliente.nome,
            "sobrenome": cliente.sobrenome,
            "perfil": cliente.perfil.value,
            "idade": cliente.idade
        }