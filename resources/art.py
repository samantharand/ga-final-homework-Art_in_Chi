import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

art = Blueprint('art', 'art')

@art.route('/', methods=['GET'])
def art_index():
	current_user_art_dicts = [ model_to_dict(art) for art in current_user.art]
	# print('sldkfjlsdkjfslkfjs')
	result = models.Art.select().dicts()
	return jsonify(
		data = current_user_art_dicts,
		message = f'Found all {len(result)} pieces of art in database',
		status = 200
	)

# create :)
@art.route('/', methods=['POST'])
def create_art():
	payload = request.get_json()
	print('CURRENT_USER LINE 21',current_user)
	print('PAYLOAD', payload)
	new_art = models.Art.create(
		name=payload['name'],
		artist=payload['artist'],
		year_made=payload['year_made'],
		current_residence=current_user.id,
	)
	print(new_art)
	art_dict = model_to_dict(new_art)
	art_dict['current_residence'].pop('password')

	return jsonify(
		data = art_dict,
		message = f"Successfully added '{art_dict['name']}' to database",
		status = 201
		), 201
	return "check term"

# destroy :(
@art.route('/<id>', methods=['DELETE'])
def delete_art(id):
	delete_query = models.Art.delete().where(models.Art.id == id)
	delete_query.execute()
	return jsonify(
		data={},
		message=f'Successfully deleted art, id#{id}',
		status=200
	), 200

# update !!!
@art.route('/<id>', methods=['PUT'])
# @login_required
def update_art(id):
	payload = request.get_json()
	art_to_update = models.Art.get_by_id(id)

	print(art_to_update)
	print(current_user)

	updated_art = models.Art.get_by_id(id)
	updated_art_dict = model_to_dict(updated_art)

	return jsonify(
		data=updated_art_dict,
		message=f'Successfully updated art, id#{id}',
		status=200
	), 200
















