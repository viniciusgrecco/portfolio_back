from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class MercadoEnum(str, Enum):
    NASDAQ = "NASDAQ"
    IBOV = "IBOV"

class Stock(BaseModel):
    """
    Entidade Stock usando Pydantic
    Representa uma ação no domínio da aplicação
    """
    id: Optional[int] = Field(
        None
    )
    ticker: str = Field(
        ...,
        min_length=1,
        max_length=10,
        description="Símbolo da ação (ex: AAPL, PETR4)"
    )
    preco_compra: float = Field(
        ...,
        gt=0,
        description="Preço de compra da ação"
    )
    mercado: MercadoEnum = Field(
        ...,
        description="Mercado da ação (NASDAQ ou IBOV)"
    )

    class Config:
        # Permite conversão de objetos SQLAlchemy para este Pydantic model
        from_attributes = True

    def __str__(self):
        return f"Stock: {self.ticker} - {self.mercado.value} (R$ {self.preco_compra:.2f})"

Stock.model_rebuild()