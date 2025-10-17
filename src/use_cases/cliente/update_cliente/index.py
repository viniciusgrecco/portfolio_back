# use_cases/cliente/update_cliente/index.py
from fastapi import APIRouter, Depends, Path
from sqlmodel import Session
from use_cases.cliente.update_cliente.update_cliente_use_case import UpdateClienteUseCase
from use_cases.cliente.update_cliente.update_cliente_dto import UpdateClienteDTO
from database import get_session

update_cliente_use_case = UpdateClienteUseCase()
router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.put(
    "/{cliente_id}",
    summary="Atualizar cliente",
    description="Atualiza os dados de um cliente existente. Apenas os campos enviados serão atualizados.",
    response_description="Cliente atualizado",
    responses={
        200: {
            "description": "Cliente atualizado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "nome": "João",
                        "sobrenome": "Silva",
                        "perfil": "agressivo",
                        "idade": 31
                    }
                }
            }
        },
        404: {"description": "Cliente não encontrado"}
    }
)
def update_cliente(
    cliente_id: int = Path(..., description="ID do cliente a ser atualizado", example=1, gt=0),
    cliente_dto: UpdateClienteDTO = ...,
    session: Session = Depends(get_session)
):
    """
    Atualiza um cliente existente.
    
    **Campos opcionais (envie apenas os que deseja atualizar):**
    - **nome**: Novo nome do cliente
    - **sobrenome**: Novo sobrenome
    - **perfil**: Novo perfil de investimento
    - **idade**: Nova idade
    """
    return update_cliente_use_case.execute(cliente_id, cliente_dto, session)