from fastapi import HTTPException
from sqlmodel import Session
from repositories.stock_repository import StockRepository

class DeleteStockUseCase:
    
    def execute(self, stock_id: int, session: Session):
        repository = StockRepository(session)
        
        stock = repository.get(stock_id)
        
        if not stock:
            raise HTTPException(
                status_code=404,
                detail=f"Stock com ID {stock_id} não encontrada"
            )
        
        repository.delete(stock)
        
        return {"message": "Stock deletada com sucesso"}