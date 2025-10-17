from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from use_cases.cliente.create_cliente.create_cliente_use_case import CreateClienteUseCase
from use_cases.cliente.create_cliente.create_cliente_dto import CreateClienteDTO
from database import get_session

create_cliente_use_case = CreateClienteUseCase()
router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Criar novo cliente",
    description="Cria um novo cliente investidor no sistema",
    response_description="Cliente criado com sucesso",
    responses={
        201: {
            "description": "Cliente criado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "nome": "João",
                        "sobrenome": "Silva",
                        "perfil": "moderado",
                        "idade": 30
                    }
                }
            }
        },
        400: {"description": "Cliente já existe ou dados inválidos"}
    }
)
def create_cliente(
    cliente_dto: CreateClienteDTO,
    session: Session = Depends(get_session)
):
    """
    Cria um novo cliente no sistema.
    
    **Campos obrigatórios:**
    - **nome**: Nome do cliente (1-45 caracteres)
    - **sobrenome**: Sobrenome do cliente (1-45 caracteres)
    - **perfil**: Perfil de investimento (conservador, moderado ou agressivo)
    - **idade**: Idade do cliente (mínimo 18 anos)
    """
    return create_cliente_use_case.execute(cliente_dto, session)