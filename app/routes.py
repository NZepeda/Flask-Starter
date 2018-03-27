from app import app
from flask import render_template
from .controllers.ImageController import ImageController

imageController = ImageController()
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', images=imageController.images)

@app.route('/picture/<image_id>')
def picture(image_id):
	print(image_id)
	return render_template('image_info.html', image=imageController.get_image_by_id(image_id))


