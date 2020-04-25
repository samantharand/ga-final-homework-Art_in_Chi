import models
from flask import Blueprint, request, jsonify

art = Blueprint('art', 'art')

@art.route('/', methods=['GET'])
def art_index():
	return 'art index reached'

@art.route('/', methods=['POST'])
def create_art():
	
	payload = request.get_json()
	print(payload)

	return 'create art route'