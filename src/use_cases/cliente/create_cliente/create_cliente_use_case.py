# use_cases/cliente/create_cliente/create_cliente_use_case.py
from fastapi import HTTPException
from sqlmodel import Session
from use_cases.cliente.create_cliente.create_cliente_dto import CreateClienteDTO
from repositories.client_repository import ClienteRepository
from models.client_model import ClienteModel, Perfil

class CreateClienteUseCase:
    
    def execute(self, cliente_dto: CreateClienteDTO, session: Session):
        repository = ClienteRepository(session)
        
        # Verifica se já existe cliente com mesmo nome e sobrenome
        existing = repository.get_by_fullname(cliente_dto.nome, cliente_dto.sobrenome)
        if existing:
            raise HTTPException(
                status_code=400,
                detail="Cliente já cadastrado com esse nome e sobrenome"
            )
        
        # Cria novo cliente
        novo_cliente = ClienteModel(
            nome=cliente_dto.nome,
            sobrenome=cliente_dto.sobrenome,
            perfil=Perfil[cliente_dto.perfil.value],
            idade=cliente_dto.idade
        )
        
        created = repository.add(novo_cliente)
        
        return {
            "id": created.id,
            "nome": created.nome,
            "sobrenome": created.sobrenome,
            "perfil": created.perfil.value,
            "idade": created.idade
        }

