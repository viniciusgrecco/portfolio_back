from fastapi import APIRouter, Depends
from sqlmodel import Session
from use_cases.stock.list_stocks.list_stocks_use_case import ListStocksUseCase
from database import get_session

list_stocks_use_case = ListStocksUseCase()
router = APIRouter(prefix="/stocks", tags=["Stocks"])

@router.get(
    "",
    summary="Listar todas as ações",
    description="Retorna uma lista com todas as ações cadastradas no sistema",
    response_description="Lista de ações",
    responses={
        200: {
            "description": "Lista de ações",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "ticker": "AAPL",
                            "preco_compra": 150.75,
                            "mercado": "NASDAQ"
                        },
                        {
                            "id": 2,
                            "ticker": "PETR4",
                            "preco_compra": 28.50,
                            "mercado": "IBOV"
                        }
                    ]
                }
            }
        }
    }
)
def list_stocks(session: Session = Depends(get_session)):
    """
    Lista todas as ações cadastradas no sistema.
    
    Retorna uma lista vazia se não houver ações cadastradas.
    """
    return list_stocks_use_case.execute(session)