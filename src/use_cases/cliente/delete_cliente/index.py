# use_cases/cliente/delete_cliente/index.py
from fastapi import APIRouter, Depends, Path, status
from sqlmodel import Session
from use_cases.cliente.delete_cliente.delete_cliente_use_case import DeleteClienteUseCase
from database import get_session

delete_cliente_use_case = DeleteClienteUseCase()
router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.delete(
    "/{cliente_id}",
    status_code=status.HTTP_200_OK,
    summary="Deletar cliente",
    description="Remove um cliente do sistema permanentemente",
    response_description="Confirmação de deleção",
    responses={
        200: {
            "description": "Cliente deletado com sucesso",
            "content": {
                "application/json": {
                    "example": {"message": "Cliente deletado com sucesso"}
                }
            }
        },
        404: {"description": "Cliente não encontrado"}
    }
)
def delete_cliente(
    cliente_id: int = Path(..., description="ID do cliente a ser deletado", example=1, gt=0),
    session: Session = Depends(get_session)
):
    """
    Deleta um cliente do sistema.
    
    **Atenção:** Esta ação é irreversível!
    
    **Parâmetros:**
    - **cliente_id**: ID do cliente a ser removido
    """
    return delete_cliente_use_case.execute(cliente_id, session)