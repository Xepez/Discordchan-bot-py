import requests
import json


class RandomCat:

    def __init__(self):
        r = requests.get('https://cataas.com/cat?json=true')
        data = json.loads(r)
        self.url = data['url']
        self.id = data['id']
        self.mimetype = data['mimetype']
        self.tags = data['tags']
        self.created_at = data['created_at']

    # Returns string of url
    def get_cat_url(self):
        await self.url

    # Returns string of id of image
    def get_cat_id(self):
        await self.id

    # Returns string of image type
    def get_cat_mimetype(self):
        await self.mimetype

    # Returns a list of strings of attributes of the cat
    def get_cat_tags(self):
        await self.tags

    # Returns a datetime of when the image was created
    def get_cat_created_at(self):
        await self.created_at
