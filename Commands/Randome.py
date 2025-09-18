import requests
import json


class Randome():

    def __init__(self, config):
        self.config = config

    # Returns string of url
    def get_random_image(self):
        r = requests.get(self.config['safebooru_base_url_test'])
        self.data = json.loads(r)

        await self.data['url']
