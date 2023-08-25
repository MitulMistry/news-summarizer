import os
import requests
from dotenv import load_dotenv

class SummaryInterface:
    """
    The SummaryInterface class is used to make API calls to the TLDRThis API and
    return a summary of an article based on a provided URL.
    """
    
    # Load environment variables from .env file for development
    load_dotenv()
    api_key = os.getenv("TLDR_API_KEY")
        

    @classmethod
    def get_extractive_summary(self, articleUrl, sentences=3):
        """
        Makes TLDRThis API call based on provided URL. Extracts key sentences from
        the article.

        :param articleUrl: The URL for the article to be summarized
        :type articleUrl: str
        :param sentences: The number of sentences to be returned
        :type sentences: int
        :returns: A list of sentences (strings)
        :rtype: list[str]
        """
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
        """
        Makes TLDRThis API call based on provided URL. Composes an AI summary based
        on the article.

        :param articleUrl: The URL for the article to be summarized
        :type articleUrl: str
        :param min_length: The minimum number of words to be returned
        :type min_length: int
        :param min_length: The maximum number of words to be returned
        :type min_length: int
        :returns: A list of sentences or paragraphs (strings)
        :rtype: list[str]
        """
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
        """
        A helper method to initiate an API call using requests

        :param url: The url to make the request to
        :type url: str
        :param payload: A dict of parameters to be included in the request
        :type payload: dict
        :param payload: A dict of headers to be included in the request
        :type payload: dict
        :raises: RequestException: If request failed
        :returns: A response object
        :rtype: requests.Response object
        """
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
        except requests.RequestException:
            return None
        
        return response


    @classmethod
    def process_response(self, response):
        """
        A helper method to process and format a Response object from requests

        :param response: The country code supported by News API
        :type response: requests.Response object
        :returns: A list of sentences or paragraphs
        :rtype: list[str]
        """
        return response.json()["summary"] if response else None

