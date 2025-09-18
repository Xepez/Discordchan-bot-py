import requests
import json


class Randome():

    def __init__(self, config):
        self.config = config

        result = requests.get('https://cataas.com/cat')
        self.cat_data = json.loads(result)

    # Returns string of url
    def get_random_image(self):
        await self.data['url']
