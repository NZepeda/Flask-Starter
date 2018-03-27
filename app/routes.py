from app import app
from flask import render_template
from .controllers.ImageController import ImageController

## Initialize the controller for the image
imageController = ImageController()

@app.route('/')
@app.route('/index')
def index():
	## Reset the images every time we refresh the index page
	imageController.reset_images()
	return render_template('index.html', images=imageController.images)

@app.route('/picture/<image_id>')
def picture(image_id):
	return render_template('image_info.html', image=imageController.get_image_by_id(image_id))

