import requests
import json


class RandomCat:

    def __init__(self):
        r = requests.get('https://cataas.com/cat?json=true')
        if r.status_code != 200:
            return None

        data = json.loads(r.text)
        self.url = data['url']  # string of url
        self.id = data['id']  # string of id of image
        self.mimetype = data['mimetype']  # string of image type
        self.tags = data['tags']  # list of strings of attributes of the cat
        self.created_at = data['created_at']  # datetime of when the image was created
