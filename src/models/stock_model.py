from enum import Enum as PyEnum
from sqlmodel import SQLModel, Field, Enum, Column
from typing import Optional

class Mercado(str, PyEnum):
    NASDAQ = "NASDAQ"
    IBOV = "IBOV"

class StockModel(SQLModel, table=True):
    __tablename__ = "stocks"

    id: Optional[int] = Field(default=None, primary_key=True)
    ticker: str = Field(max_length=10, index=True)
    preco_compra: float = Field()
    mercado: Mercado = Field(sa_column=Column(Enum(Mercado), nullable=False, index=True))

    def __repr__(self):
        return (f"<StockModel(id={self.id}, ticker='{self.ticker}', "
                f"preco_compra={self.preco_compra}, mercado='{self.mercado.value if self.mercado else None}')>")