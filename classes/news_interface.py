import os
import requests
from dotenv import load_dotenv

import urllib.parse
from datetime import datetime, timedelta

class NewsInterface:
    def __init__(self):
        # Load environment variables from .env file for development
        load_dotenv()
        self.api_key = os.getenv("NEWS_API_KEY")
        
    
    def get_articles_by_country(self, country="us", count=5):
        payload = {"country": country, "apiKey": self.api_key}

        response = self.make_request("https://newsapi.org/v2/top-headlines", payload)
        
        return self.process_response(response, count)
    

    def get_articles_by_source(self, source="abc-news", count=5):
        payload = {"source": source, "apiKey": self.api_key}

        response = self.make_request("https://newsapi.org/v2/top-headlines", payload)
        
        return self.process_response(response, count)

    
    def get_articles_by_search(self, search_str, count=5, days=7):
        date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

        payload = {
            "q": urllib.parse.quote_plus(search_str[:30]),
            "from": date,
            "sortBy": "popularity",
            "apiKey": self.api_key
        }

        response = self.make_request("https://newsapi.org/v2/everything", payload)
        
        return self.process_response(response, count)


    def make_request(self, url, params):
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.RequestException:
            return None
        
        return response


    def process_response(self, response, count=5):
        return response.json()["articles"][:count] if response else None

