import os

class Image:
    def __init__(self, imageData):
        self.id = imageData["id"]
        self.title = imageData["title"]
        self.flickr_user = imageData["flickr_user"]
        self.tags = imageData["tags"]

    def get_path(self):
        return self.id + '.jpg'
