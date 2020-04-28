from flask import Flask, jsonify

from resources.art import art
from resources.museum import museum
import models
from flask_cors import CORS
from flask_login import LoginManager

DEBUG=True
PORT=8000


app = Flask(__name__)

# configure login manager
app.secret_key = 'Temp'
login_manager = LoginManager()
login_manager.init_app(app)

CORS(art, origins=['http://localhost:3000'], support_credentials=True)
CORS(museum, origins=['http://localhost:3000'], support_credentials=True)

app.register_blueprint(art, url_prefix='/api/v1/art')
app.register_blueprint(museum, url_prefix='/api/v1/museum')

@app.route('/')
def landing_page():
	return "hit the landing page, killin itttt"










if __name__ == '__main__':
	models.init() 

	app.run(debug=DEBUG, port=PORT)