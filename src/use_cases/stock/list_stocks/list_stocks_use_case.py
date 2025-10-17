from sqlmodel import Session
from repositories.stock_repository import StockRepository

class ListStocksUseCase:
    
    def execute(self, session: Session):
        repository = StockRepository(session)
        
        stocks = repository.list()
        
        return [
            {
                "id": stock.id,
                "ticker": stock.ticker,
                "preco_compra": stock.preco_compra,
                "mercado": stock.mercado.value
            }
            for stock in stocks
        ]
