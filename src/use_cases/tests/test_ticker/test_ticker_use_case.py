# use_cases/tests/test_ticker/test_ticker_use_case.py
from fastapi import Response, Request
from collections import Counter
from utils.news_ticker_api import get_ticker_info  # assumindo que agora aceita um str

class TestTickerUseCase:

    def execute(self, response: Response, request: Request, ticker: str):
        """
        Executa a lógica de coleta/agregação de notícias para o ticker informado.
        `ticker` deve ser uma string como "AAPL".
        """
        if not ticker or not isinstance(ticker, str):
            return {"status": 400, "message": "Ticker inválido"}

        ticker_upper = ticker.upper()

        # chama util (assumi que get_ticker_info aceita simplesmente o ticker string)
        data = get_ticker_info(ticker_upper)
        print("saiu do utils")

        feed = data.get("feed", []) if isinstance(data, dict) else []

        if not feed:
            return {
                "status": 200,
                "ticker": ticker_upper,
                "news_count": 0,
                "sentiment": {
                    "score": 0,
                    "label": "Neutral",
                    "min": 0,
                    "max": 0
                },
                "top_topics": [],
                "message": "Nenhuma notícia encontrada para este ticker"
            }

        sentiment_scores = []
        topic_counter = Counter()
        news_count = 0

        for article in feed:
            ticker_sentiments = article.get("ticker_sentiment", [])
            for ticker_data in ticker_sentiments:
                if ticker_data.get("ticker") == ticker_upper:
                    news_count += 1

                    sentiment_score = ticker_data.get("ticker_sentiment_score", 0)
                    try:
                        sentiment_score = float(sentiment_score)
                        sentiment_scores.append(sentiment_score)
                    except (ValueError, TypeError):
                        # ignora valores inválidos
                        pass

                    topics = article.get("topics", [])
                    for topic in topics:
                        topic_name = topic.get("topic")
                        if topic_name:
                            topic_counter[topic_name] += 1
                    break  # já encontrou esse ticker para o artigo, passa pro próximo artigo

        if sentiment_scores:
            avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
            min_sentiment = min(sentiment_scores)
            max_sentiment = max(sentiment_scores)
        else:
            avg_sentiment = 0
            min_sentiment = 0
            max_sentiment = 0

        if avg_sentiment <= -0.35:
            sentiment_label = "Bearish"
        elif avg_sentiment <= -0.15:
            sentiment_label = "Somewhat-Bearish"
        elif avg_sentiment < 0.15:
            sentiment_label = "Neutral"
        elif avg_sentiment < 0.35:
            sentiment_label = "Somewhat-Bullish"
        else:
            sentiment_label = "Bullish"

        top_topics = [{"topic": topic, "count": count} for topic, count in topic_counter.most_common(5)]

        return {
            "status": 200,
            "ticker": ticker_upper,
            "news_count": news_count,
            "sentiment": {
                "score": round(avg_sentiment, 6),
                "label": sentiment_label,
                "min": round(min_sentiment, 6),
                "max": round(max_sentiment, 6)
            },
            "top_topics": top_topics
        }
