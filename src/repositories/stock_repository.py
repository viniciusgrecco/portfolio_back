from sqlmodel import Session, select
from typing import List
from models.stock_model import StockModel, Mercado
from repositories.base_repository import BaseRepository

class StockRepository(BaseRepository[StockModel]):
    def __init__(self, session: Session):
        super().__init__(session, StockModel)

    def get_by_ticker(self, ticker: str) -> List[StockModel]:
        """Busca todas as ações por ticker exato"""
        statement = select(StockModel).where(StockModel.ticker == ticker.upper())
        results = self.session.exec(statement)
        return results.all()

    def get_by_mercado(self, mercado: Mercado) -> List[StockModel]:
        """Retorna lista de ações por mercado (NASDAQ/IBOV)"""
        statement = select(StockModel).where(StockModel.mercado == mercado)
        results = self.session.exec(statement)
        return results.all()

    def get_by_ticker_partial(self, ticker_fragment: str) -> List[StockModel]:
        """Busca ações onde o ticker contenha o fragmento (case-insensitive)"""
        statement = select(StockModel).where(StockModel.ticker.contains(ticker_fragment.upper()))
        results = self.session.exec(statement)
        return results.all()

    def get_by_preco_range(self, preco_min: float, preco_max: float) -> List[StockModel]:
        """Retorna ações dentro de uma faixa de preço"""
        statement = select(StockModel).where(
            StockModel.preco_compra >= preco_min,
            StockModel.preco_compra <= preco_max
        )
        results = self.session.exec(statement)
        return results.all()