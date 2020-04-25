from flask import Flask, jsonify

DEBUG=True
PORT=8000

app = Flask(__name__)

@app.route('/')
def landing_page():
	return "hit the landing page, killin itttt"


if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)