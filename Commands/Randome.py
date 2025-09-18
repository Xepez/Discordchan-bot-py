import requests
import json
import random as rand

class Randome():

    def __init__(self, config):
        self.config = config
        self.id = 0
        self.tag_string = ""


    # region Old


    # Returns string of url
    async def get_random_image(self):
        end_url = '/posts/random.json' #  ?tags=' + [tags] #  can we add tags?
        r = requests.get(self.config['safebooru_base_url_test']+ '/' + end_url)
        if r.status_code != 200:
            await None

        self.data = json.loads(r.data)
        return await self.data['file_url']


    # endregion
