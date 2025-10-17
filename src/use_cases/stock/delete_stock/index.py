from fastapi import APIRouter, Depends, Path, status
from sqlmodel import Session
from use_cases.stock.delete_stock.delete_stock_use_case import DeleteStockUseCase
from database import get_session

delete_stock_use_case = DeleteStockUseCase()
router = APIRouter(prefix="/stocks", tags=["Stocks"])

@router.delete(
    "/{stock_id}",
    status_code=status.HTTP_200_OK,
    summary="Deletar ação",
    description="Remove uma ação do sistema permanentemente",
    response_description="Confirmação de deleção",
    responses={
        200: {
            "description": "Ação deletada com sucesso",
            "content": {
                "application/json": {
                    "example": {"message": "Stock deletada com sucesso"}
                }
            }
        },
        404: {"description": "Ação não encontrada"}
    }
)
def delete_stock(
    stock_id: int = Path(..., description="ID da ação a ser deletada", example=1, gt=0),
    session: Session = Depends(get_session)
):
    """
    Deleta uma ação do sistema.
    
    **Atenção:** Esta ação é irreversível!
    
    **Parâmetros:**
    - **stock_id**: ID da ação a ser removida
    """
    return delete_stock_use_case.execute(stock_id, session)