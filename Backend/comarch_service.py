import requests
import json
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

class ComarchService:
    def __init__(self):
        self.api_url = os.getenv('COMARCH_API_URL')
        self.api_key = os.getenv('COMARCH_API_KEY')

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def fetch_product_data(self, product_id):
        try:
            response = requests.get(f'{self.api_url}/products/{product_id}', headers=self.get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f'Error fetching product data: {e}')
            return None

    def update_product_data(self, product_id, data):
        try:
            payload = json.dumps(data)
            response = requests.put(f'{self.api_url}/products/{product_id}', headers=self.get_headers(), data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f'Error updating product data: {e}')
            return None
