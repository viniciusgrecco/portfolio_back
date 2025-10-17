# use_cases/stock/create_stock/create_stock_use_case.py
from sqlmodel import Session
from use_cases.stock.create_stock.create_stock_dto import CreateStockDTO
from repositories.stock_repository import StockRepository
from models.stock_model import StockModel, Mercado

class CreateStockUseCase:
    
    def execute(self, stock_dto: CreateStockDTO, session: Session):
        repository = StockRepository(session)
        
        # Cria nova stock
        nova_stock = StockModel(
            ticker=stock_dto.ticker.upper(),
            preco_compra=stock_dto.preco_compra,
            mercado=Mercado[stock_dto.mercado.value]
        )
        
        created = repository.add(nova_stock)
        
        return {
            "id": created.id,
            "ticker": created.ticker,
            "preco_compra": created.preco_compra,
            "mercado": created.mercado.value
        }
