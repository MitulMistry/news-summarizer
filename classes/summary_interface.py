import os
import requests
from dotenv import load_dotenv

class SummaryInterface:
    # Load environment variables from .env file for development
    load_dotenv()
    api_key = os.getenv("TLDR_API_KEY")
        

    @classmethod
    def get_extractive_summary(self, articleUrl, sentences=3):    
        apiUrl = "https://tldrthis.p.rapidapi.com/v1/model/extractive/summarize-url/"

        payload = {
            "url": articleUrl,
            "num_sentences": sentences,
            "is_detailed": False
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "tldrthis.p.rapidapi.com"
        }
        
        response = self.make_request(apiUrl, payload, headers)        
        return self.process_response(response)


    @classmethod
    def get_humanlike_summary(self, articleUrl, min_length=50, max_length=100):
        apiUrl = "https://tldrthis.p.rapidapi.com/v1/model/abstractive/summarize-url/"

        payload = {
            "url": articleUrl,
            "min_length": min_length,
            "max_length": max_length,
            "is_detailed": False
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "tldrthis.p.rapidapi.com"
        }

        response = self.make_request(apiUrl, payload, headers)
        return self.process_response(response)


    @classmethod
    def make_request(self, url, payload, headers):
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
        except requests.RequestException:
            return None
        
        return response


    @classmethod
    def process_response(self, response):
        """
        Returns a list of sentences/paragraphs, or None if empty response
        """
        return response.json()["summary"] if response else None

