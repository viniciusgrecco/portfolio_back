from fastapi import Response, Request
import requests
import dotenv
import os
from collections import Counter
from utils.news_api import get_news_test


class TestUseCase:

    def execute(self, response: Response, request: Request):
        
        
        data = get_news_test()
        feed = data.get("feed", [])
        
        nvda_sentiment_scores = []
        topic_counter = Counter()
        news_count = 0
        
        for article in feed:
            
            ticker_sentiments = article.get("ticker_sentiment", [])
            
            for ticker_data in ticker_sentiments:
                if ticker_data.get("ticker") == "NVDA":
                    news_count += 1
            
                    sentiment_score = ticker_data.get("ticker_sentiment_score", 0)
                    try:
                        sentiment_score = float(sentiment_score)
                        nvda_sentiment_scores.append(sentiment_score)
                    except (ValueError, TypeError):
            
                        pass
                    
            
                    topics = article.get("topics", [])
                    for topic in topics:
                        topic_name = topic.get("topic")
                        if topic_name:
                            topic_counter[topic_name] += 1
                    break
        
        
        if nvda_sentiment_scores:
            avg_sentiment = sum(nvda_sentiment_scores) / len(nvda_sentiment_scores)
            min_sentiment = min(nvda_sentiment_scores)
            max_sentiment = max(nvda_sentiment_scores)
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
            "ticker": "NVDA",
            "news_count": news_count,
            "sentiment": {
                "score": round(avg_sentiment, 6),
                "label": sentiment_label,
                "min": round(min_sentiment, 6),
                "max": round(max_sentiment, 6)
            },
            "top_topics": top_topics
        }
