from fastapi import APIRouter, Depends, Path
from sqlmodel import Session
from use_cases.stock.update_stock.update_stock_use_case import UpdateStockUseCase
from use_cases.stock.update_stock.update_stock_dto import UpdateStockDTO
from database import get_session

update_stock_use_case = UpdateStockUseCase()
router = APIRouter(prefix="/stocks", tags=["Stocks"])

@router.put(
    "/{stock_id}",
    summary="Atualizar ação",
    description="Atualiza os dados de uma ação existente. Apenas os campos enviados serão atualizados.",
    response_description="Ação atualizada",
    responses={
        200: {
            "description": "Ação atualizada com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "ticker": "AAPL",
                        "preco_compra": 155.50,
                        "mercado": "NASDAQ"
                    }
                }
            }
        },
        404: {"description": "Ação não encontrada"}
    }
)
def update_stock(
    stock_id: int = Path(..., description="ID da ação a ser atualizada", example=1, gt=0),
    stock_dto: UpdateStockDTO = ...,
    session: Session = Depends(get_session)
):
    """
    Atualiza uma ação existente.
    
    **Campos opcionais (envie apenas os que deseja atualizar):**
    - **ticker**: Novo símbolo da ação
    - **preco_compra**: Novo preço de compra
    - **mercado**: Novo mercado (NASDAQ ou IBOV)
    """
    return update_stock_use_case.execute(stock_id, stock_dto, session)