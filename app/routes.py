## Nestor Zepeda
## 3/26/18
## CST 205

## Main routes file for the application. 
## This is a simple app containing two distinct routes
from app import app
from flask import render_template
from .controllers.ImageController import ImageController

## Initialize the controller for the image
imageController = ImageController()

@app.route('/')
@app.route('/index')
def index():
	## Reset the images every time we refresh the index page
	print("Reseting images!")
	imageController.reset_images()
	return render_template('index.html', images=imageController.images)

@app.route('/picture/<image_id>')
def picture(image_id):
	return render_template('image_info.html', image=imageController.get_image_by_id(image_id))

