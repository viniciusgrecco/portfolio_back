from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from use_cases.stock.create_stock.create_stock_use_case import CreateStockUseCase
from use_cases.stock.create_stock.create_stock_dto import CreateStockDTO
from database import get_session

create_stock_use_case = CreateStockUseCase()
router = APIRouter(prefix="/stocks", tags=["Stocks"])

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Criar nova ação",
    description="Registra uma nova ação comprada no sistema",
    response_description="Ação criada com sucesso",
    responses={
        201: {
            "description": "Ação criada com sucesso",
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
        400: {"description": "Dados inválidos"}
    }
)
def create_stock(
    stock_dto: CreateStockDTO,
    session: Session = Depends(get_session)
):
    """
    Cria uma nova ação no sistema.
    
    **Campos obrigatórios:**
    - **ticker**: Símbolo da ação (ex: AAPL, PETR4) - será convertido para maiúsculas
    - **preco_compra**: Preço de compra da ação (deve ser maior que 0)
    - **mercado**: Mercado da ação (NASDAQ ou IBOV)
    """
    return create_stock_use_case.execute(stock_dto, session)