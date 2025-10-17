from pydantic import BaseModel, Field
from entities.stock import MercadoEnum

class CreateStockDTO(BaseModel):
    """DTO para criação de stock"""
    ticker: str = Field(..., min_length=1, max_length=10, description="Símbolo da ação", example="AAPL")
    preco_compra: float = Field(..., gt=0, description="Preço de compra da ação", example=150.75)
    mercado: MercadoEnum = Field(..., description="Mercado da ação", example="NASDAQ")
