from typing import List, Dict
from Functions.api_client import ApiClient

class Repository:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def get_posts(self) -> List[Dict]:
        return self.api_client.get_data('posts')

    def get_users(self) -> List[Dict]:
        return self.api_client.get_data('users')
