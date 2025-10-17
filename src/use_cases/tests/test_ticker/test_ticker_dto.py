from pydantic import BaseModel

class TestTickerDTO(BaseModel):
    ticker : str