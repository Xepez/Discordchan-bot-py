import requests
import json


class RandomCat:

    def __init__(self):
        r = requests.get('https://cataas.com/cat?json=true')
        if r.status_code != 200:
            return None

        data = json.loads(r.text)
        self.url = data['url']
        self.id = data['id']
        self.mimetype = data['mimetype']
        self.tags = data['tags']
        self.created_at = data['created_at']

    # Returns string of url
    async def get_cat_url(self):
        return self.url

    # Returns string of id of image
    async def get_cat_id(self):
        return self.id

    # Returns string of image type
    async def get_cat_mimetype(self):
        return self.mimetype

    # Returns a list of strings of attributes of the cat
    async def get_cat_tags(self):
        return self.tags

    # Returns a datetime of when the image was created
    async def get_cat_created_at(self):
        return self.created_at
