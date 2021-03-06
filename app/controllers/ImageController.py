## Nestor Zepeda
## 3/26/18
## CST 205

## A controller to manage images 

from image_information import image_info
from ..models.Image import Image
import random

class ImageController:
    
    def __init__(self):
        self.images = self.get_images()

    def reset_images(self):
        self.images = self.get_images()

    def get_images(self):
        ## Use a set to store randomly created indeces between 0 and 10 to ensure 
        ## we don't have duplicates
        index_set = set()
        image_list = []

        while len(index_set) < 3:
            
            random_index = random.randint(0, len(image_info) - 1)

            if(random_index not in index_set):
                index_set.add(random_index)
                image_list.append(Image(image_info[random_index]))
        
        return image_list
    
    def get_image_by_id(self, id):
        for image in image_info:
            if(image["id"] == id):
                return Image(image)

        print("Couldn't find image with id: {id}".format(id=id))
        return None


        
