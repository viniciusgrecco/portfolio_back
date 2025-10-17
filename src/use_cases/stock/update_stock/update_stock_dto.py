from pydantic import BaseModel, Field
from typing import Optional
from entities.stock import MercadoEnum

class UpdateStockDTO(BaseModel):
    """DTO para atualização de stock"""
    ticker: Optional[str] = Field(None, min_length=1, max_length=10, description="Novo símbolo da ação", example="AAPL")
    preco_compra: Optional[float] = Field(None, gt=0, description="Novo preço de compra", example=155.50)
    mercado: Optional[MercadoEnum] = Field(None, description="Novo mercado", example="NASDAQ")
