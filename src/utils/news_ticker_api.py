import os
import requests

def get_ticker_info(ticker: str):
    """
    Busca informações de notícias e sentimento para o ticker informado.
    
    Args:
        ticker (str): símbolo do ticker (ex: "AAPL").
    """
    print("entrou no utils")

    api_key = os.environ.get("NEWS_API_KEY")
    ticker = ticker.upper()

    EXTERNAL_API = (
        f"https://www.alphavantage.co/query?"
        f"function=NEWS_SENTIMENT&tickers={ticker}"
        f"&time_from=20250906T0000&time_to=20251006T2359"
        f"&limit=1000&sort=LATEST&apikey={api_key}"
    )

    response = requests.get(EXTERNAL_API)
    response.raise_for_status()
    data = response.json()
    
    return data
