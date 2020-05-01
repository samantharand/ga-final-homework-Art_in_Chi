import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

art = Blueprint('art', 'art')

@art.route('/', methods=['GET'])
@login_required
def art_index():
	current_user_art_dicts = [ model_to_dict(art) for art in current_user.art]
	# print('sldkfjlsdkjfslkfjs')
	result = models.Art.select().dicts()
	return jsonify(
		data = current_user_art_dicts,
		message = f'Found your art in database',
		status = 200
	)

# create :)
@art.route('/', methods=['POST'])
@login_required
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
@login_required
def delete_art(id):
	art_to_delete = models.Art.get_by_id(id)
	art_to_delete_dict = model_to_dict(art_to_delete)

	if current_user.id == art_to_delete_dict['current_residence']['id']:
		art_to_delete.delete_instance()


		return jsonify(
			data={},
			message=f'Successfully deleted art, id#{id}',
			status=200
		), 200
	else:
		return jsonify(
			data= {},
			message="thats not ur art",
			status=403
		), 403
# update !!!
@art.route('/<id>', methods=['PUT'])
@login_required
def update_the_art(id):
	payload = request.get_json()
	art_to_update = models.Art.get_by_id(id)
	art_to_update_dict = model_to_dict(art_to_update)

	if current_user.id == art_to_update_dict['current_residence']['id']:

		art_to_update_dict['name'] = payload['name']
		art_to_update_dict['artist'] = payload['artist']
		art_to_update_dict['year_made'] = payload['year_made']

		art_to_update_dict['current_residence'].pop('password')

		

		return jsonify(
			data=art_to_update_dict,
			message=f'Successfully updated art, id#{id}',
			status=200
		), 200
	else:
		return jsonify(
			data= {},
			message="thats not ur art",
			status=403
		), 403
	# return "check term"
















