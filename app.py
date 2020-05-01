from flask import Flask, jsonify

from resources.art import art
from resources.museum import museum
import models
from flask_cors import CORS, logging
from flask_login import LoginManager

DEBUG=True
PORT=8000


app = Flask(__name__)

# configure login manager
app.secret_key = 'Temp'
login_manager = LoginManager()
login_manager.init_app(app)

# user loader
@login_manager.user_loader
def load_user(user_id):
	try:
		museum = models.Museum.get_by_id(user_id)
		return museum
	except models.DoesNotExist:
		return None

@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(
		data={'error': 'not logged in'},
		message='u gotta be logged in, dude',
		status=404
	), 404

## TROUBLE SHOOTING 
logging.getLogger('flask_cors').level = logging.DEBUG

CORS(art, origins=['http://localhost:3000'], supports_credentials=True)
CORS(museum, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(art, url_prefix='/api/v1/art')
app.register_blueprint(museum, url_prefix='/api/v1/museum')

@app.route('/')
def landing_page():
	return "hit the landing page, killin itttt"










if __name__ == '__main__':
	models.init() 

	app.run(debug=DEBUG, port=PORT)