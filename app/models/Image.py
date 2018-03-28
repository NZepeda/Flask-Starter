## Nestor Zepeda
## 3/26/18
## CST 205

## Image class for when we read image info from the gist provided for this assignment


import os
from PIL import Image as Pillow

class Image:
    def __init__(self, imageData):
        self.id = imageData["id"]
        self.title = imageData["title"]
        self.flickr_user = imageData["flickr_user"]
        self.tags = imageData["tags"]

    def get_path(self):
        return self.id + '.jpg'

    def get_image_info(self):

        ## Image path should not be statically coded like this. 
        ## TODO: Find a better method of getting path to image
        ##       Even better, store images in AWS S3 bucket.
        image_path = os.path.abspath('app/static/' + self.id + '.jpg')
        image = Pillow.open(image_path)

        return "{mode} image in {format} format with width {width} and height {height}".format(
            mode = image.mode, 
            format = image.format, 
            width=image.width, 
            height=image.height)

