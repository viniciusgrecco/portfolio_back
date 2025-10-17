# use_cases/cliente/delete_cliente/delete_cliente_use_case.py
from fastapi import HTTPException
from sqlmodel import Session
from repositories.client_repository import ClienteRepository

class DeleteClienteUseCase:
    
    def execute(self, cliente_id: int, session: Session):
        repository = ClienteRepository(session)
        
        cliente = repository.get(cliente_id)
        
        if not cliente:
            raise HTTPException(
                status_code=404,
                detail=f"Cliente com ID {cliente_id} não encontrado"
            )
        
        repository.delete(cliente)
        
        return {"message": "Cliente deletado com sucesso"}