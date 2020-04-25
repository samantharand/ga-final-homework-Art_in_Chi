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
	new_art = models.Art.create(
		name=payload['name'],
		artist=payload['artist'],
		year_made=payload['year_made'],
		current_residence=payload['current_residence'],
	)
	print(new_art)

	return 'create art route'