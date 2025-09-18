import requests
import json
import random as rand


class Randome:

    def __init__(self, config):
        self.config = config

    # region New

    async def get_random_image_2(self):
        random_num = rand.randint(1, self.config['safebooru_base_post_cap'])
        end_url = f'index.php?page=post&s=view&id={random_num}&json=1'
        r = requests.get(self.config['safebooru_base_url'] + end_url)
        if r.status_code != 200 or r.url == 'https://safebooru.org/index.php?page=post&s=list&tags=all':
            await None

        return r.url

    # endregion

    # region Old

    async def get_random_image(self):
        end_url = '/posts/random.json'  # ?tags=' + [tags] #  can we add tags?
        r = requests.get(self.config['safebooru_base_url_test'] + end_url)
        if r.status_code != 200:
            await None

        data = json.loads(r.text)
        return data['file_url']

    # endregion
