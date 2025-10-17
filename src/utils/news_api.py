import os
import requests


def get_news_test():
    api_key = os.environ.get("NEWS_API_KEY")
    EXTERNAL_API = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=NVDA&time_from=20250909T0000&time_to=20251006T2359&limit=1000&sort=LATEST&apikey={api_key}"

    response = requests.get(EXTERNAL_API)
    response.raise_for_status()
    data = response.json()

    return data