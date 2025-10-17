from fastapi import APIRouter, Depends, Path
from sqlmodel import Session
from use_cases.stock.get_stock.get_stock_use_case import GetStockUseCase
from database import get_session

get_stock_use_case = GetStockUseCase()
router = APIRouter(prefix="/stocks", tags=["Stocks"])

@router.get(
    "/{stock_id}",
    summary="Buscar ação por ID",
    description="Retorna os dados de uma ação específica pelo ID",
    response_description="Dados da ação",
    responses={
        200: {
            "description": "Ação encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "ticker": "AAPL",
                        "preco_compra": 150.75,
                        "mercado": "NASDAQ"
                    }
                }
            }
        },
        404: {"description": "Ação não encontrada"}
    }
)
def get_stock(
    stock_id: int = Path(..., description="ID único da ação", example=1, gt=0),
    session: Session = Depends(get_session)
):
    """
    Busca uma ação específica pelo ID.
    
    **Parâmetros:**
    - **stock_id**: ID único da ação no sistema
    """
    return get_stock_use_case.execute(stock_id, session)