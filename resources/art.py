import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

art = Blueprint('art', 'art')

@art.route('/', methods=['GET'])
def art_index():
	result = models.Art.select().dicts()
	return jsonify(
		data = [art for art in result],
		message = 'Found all art in database',
		status = 200
	)

@art.route('/', methods=['POST'])
def create_art():
	payload = request.get_json()
	# print(payload)
	new_art = models.Art.create(
		name=payload['name'],
		artist=payload['artist'],
		year_made=payload['year_made'],
		current_residence=payload['current_residence'],
	)
	# print(new_art)
	art_dict = model_to_dict(new_art)
	print("")
	print("art_dict")
	print(art_dict)

	return jsonify(
		data = art_dict,
		message = f"Successfully added '{art_dict['name']}' to database",
		status = 201
		), 201