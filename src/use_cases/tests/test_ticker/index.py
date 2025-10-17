# use_cases/tests/test_ticker/index.py
from fastapi import APIRouter, Response, Request, Path
from use_cases.tests.test_ticker.test_ticker_use_case import TestTickerUseCase

test_ticker_use_case = TestTickerUseCase()
router = APIRouter(prefix="/get", tags=["Tickers"])

@router.get(
    "/one/ticker/{ticker}",
    summary="Buscar dados de um ticker",
    description="Retorna estatísticas de notícias e sentimento para o ticker informado (ex: AAPL).",
    response_description="Resumo de sentimento e top topics para o ticker",
    responses={
        200: {
            "description": "Resumo de ticker retornado",
            "content": {
                "application/json": {
                    "example": {
                        "status": 200,
                        "ticker": "AAPL",
                        "news_count": 12,
                        "sentiment": {
                            "score": 0.123456,
                            "label": "Somewhat-Bullish",
                            "min": -0.5,
                            "max": 0.8
                        },
                        "top_topics": [
                            {"topic": "earnings", "count": 5},
                            {"topic": "merger", "count": 3}
                        ]
                    }
                }
            }
        },
        404: {"description": "Ticker não encontrado"},
        400: {"description": "Ticker inválido"}
    }
)
def get_one_ticker(
    ticker: str = Path(..., description="Símbolo do ticker (ex: AAPL)", example="AAPL"),
    response: Response = None,
    request: Request = None
):
    """
    Busca informações de notícias/sentimento para o ticker informado na rota.
    """
    return test_ticker_use_case.execute(response, request, ticker)
