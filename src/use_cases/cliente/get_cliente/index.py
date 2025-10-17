#use_cases/cliente/get_cliente/index.py
from fastapi import APIRouter, Depends, Path
from sqlmodel import Session
from use_cases.cliente.get_cliente.get_cliente_use_case import GetClienteUseCase
from database import get_session

get_cliente_use_case = GetClienteUseCase()
router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get(
    "/{cliente_id}",
    summary="Buscar cliente por ID",
    description="Retorna os dados de um cliente específico pelo ID",
    response_description="Dados do cliente",
    responses={
        200: {
            "description": "Cliente encontrado",
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
        404: {"description": "Cliente não encontrado"}
    }
)
def get_cliente(
    cliente_id: int = Path(..., description="ID único do cliente", example=1, gt=0),
    session: Session = Depends(get_session)
):
    """
    Busca um cliente específico pelo ID.
    
    **Parâmetros:**
    - **cliente_id**: ID único do cliente no sistema
    """
    return get_cliente_use_case.execute(cliente_id, session)