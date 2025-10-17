from fastapi import HTTPException
from sqlmodel import Session
from use_cases.stock.update_stock.update_stock_dto import UpdateStockDTO
from repositories.stock_repository import StockRepository
from models.stock_model import Mercado

class UpdateStockUseCase:
    
    def execute(self, stock_id: int, stock_dto: UpdateStockDTO, session: Session):
        repository = StockRepository(session)
        
        stock = repository.get(stock_id)
        
        if not stock:
            raise HTTPException(
                status_code=404,
                detail=f"Stock com ID {stock_id} não encontrada"
            )
        
        # Atualiza apenas os campos fornecidos
        if stock_dto.ticker is not None:
            stock.ticker = stock_dto.ticker.upper()
        if stock_dto.preco_compra is not None:
            stock.preco_compra = stock_dto.preco_compra
        if stock_dto.mercado is not None:
            stock.mercado = Mercado[stock_dto.mercado.value]
        
        updated = repository.update(stock)
        
        return {
            "id": updated.id,
            "ticker": updated.ticker,
            "preco_compra": updated.preco_compra,
            "mercado": updated.mercado.value
        }
