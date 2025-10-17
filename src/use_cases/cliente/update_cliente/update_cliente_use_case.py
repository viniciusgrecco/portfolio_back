# use_cases/cliente/update_cliente/update_cliente_use_case.py
from fastapi import HTTPException
from sqlmodel import Session
from use_cases.cliente.update_cliente.update_cliente_dto import UpdateClienteDTO
from repositories.client_repository import ClienteRepository
from models.client_model import Perfil

class UpdateClienteUseCase:
    
    def execute(self, cliente_id: int, cliente_dto: UpdateClienteDTO, session: Session):
        repository = ClienteRepository(session)
        
        cliente = repository.get(cliente_id)
        
        if not cliente:
            raise HTTPException(
                status_code=404,
                detail=f"Cliente com ID {cliente_id} não encontrado"
            )
        
        # Atualiza apenas os campos fornecidos
        if cliente_dto.nome is not None:
            cliente.nome = cliente_dto.nome
        if cliente_dto.sobrenome is not None:
            cliente.sobrenome = cliente_dto.sobrenome
        if cliente_dto.perfil is not None:
            cliente.perfil = Perfil[cliente_dto.perfil.value]
        if cliente_dto.idade is not None:
            cliente.idade = cliente_dto.idade
        
        updated = repository.update(cliente)
        
        return {
            "id": updated.id,
            "nome": updated.nome,
            "sobrenome": updated.sobrenome,
            "perfil": updated.perfil.value,
            "idade": updated.idade
        }
