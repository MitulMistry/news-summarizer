import os
import requests
from dotenv import load_dotenv

import urllib.parse
from datetime import datetime, timedelta

class NewsInterface:
    """
    The NewsInterface class is used to make API calls to the News API and
    return articles.
    """

    # Load environment variables from .env file for development
    load_dotenv()
    api_key = os.getenv("NEWS_API_KEY")
        

    @classmethod
    def get_articles_by_country(self, country="us", count=5):
        """
        Makes News API call based on provided country code

        :param country: The country code supported by News API
        :type country: str
        :param count: The number of articles meant to be returned (up to 10)
        :type count: int
        :returns: A list of articles
        :rtype: list[dict]
        """
        payload = {"country": country, "apiKey": self.api_key}
        response = self.make_request("https://newsapi.org/v2/top-headlines", payload)        
        return self.process_response(response, count)
    

    @classmethod
    def get_articles_by_source(self, source="abc-news", count=5):
        """
        Makes News API call based on provided news source code

        :param source: The source code supported by News API
        :type source: str
        :param count: The number of articles meant to be returned (up to 10)
        :type count: int
        :returns: A list of articles
        :rtype: list[dict]
        """
        payload = {"sources": source, "apiKey": self.api_key}
        response = self.make_request("https://newsapi.org/v2/top-headlines", payload)        
        return self.process_response(response, count)


    @classmethod
    def get_articles_by_search(self, search_str, count=5, days=7):
        """
        Makes News API call based on a search query

        :param search_str: A search query string
        :type search_str: str
        :param count: The number of articles meant to be returned (up to 10)
        :type count: int
        :param days: The number of days previous to today to include results for
        :type days: int
        :returns: A list of articles
        :rtype: list[dict]
        """
        date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

        payload = {
            "q": urllib.parse.quote_plus(search_str[:30]),
            "from": date,
            "sortBy": "popularity",
            "apiKey": self.api_key
        }

        response = self.make_request("https://newsapi.org/v2/everything", payload)        
        return self.process_response(response, count)


    @classmethod
    def make_request(self, url, params):
        """
        A helper method to initiate an API call using requests

        :param url: The url to make the request to
        :type url: str
        :param params: A dict of parameters to be embedded in the request string
        :type params: dict
        :raises: RequestException: If request failed
        :returns: A response object
        :rtype: requests.Response object
        """
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.RequestException:
            return None
        
        return response


    @classmethod
    def process_response(self, response, count=5):
        """
        A helper method to process and format a Response object from requests

        :param response: The country code supported by News API
        :type response: requests.Response object
        :param count: The number of articles meant to be returned (up to 10)
        :type count: int
        :returns: A list of articles
        :rtype: list[dict]
        """
        return response.json()["articles"][:count] if response else None

