from image_information import image_info
from ..models.Image import Image
import random

class ImageController:
    
    def __init__(self):
        self.images = self.get_images()

    def get_images(self):
        image_list = []
        index_set = set()

        ## Use a set to store randomly created indeces between 0 and 10 to ensure 
        ## we don't have duplicates
        while len(index_set) < 3:
            index_set.add(random.randint(0, len(image_info) - 1))
        
        for index in index_set:
            image_list.append(Image(image_info[index]))

        return image_list
    
    def get_image_by_id(self, id):
        for image in self.images:
            if(image.id == id):
                return image
        return None


        
