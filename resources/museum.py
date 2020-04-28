import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user

museum = Blueprint('museum', 'museum')

# test route
@museum.route('/', methods=['GET'])
def test():
	return 'yayyyy museum test route works'

# register your museum
@museum.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	payload['name'] = payload['name'].lower()
	payload['email'] = payload['email'].lower()

	try:
		models.Museum.get(models.Museum['email'] == payload['email'])
		
		return jsonify (
			data={},
			message=f'{payload["email"]} is already registered',
			status=401
		), 401
	
	except models.DoesNotExist:

		try:
			# name of museum
			models.Museum.get(models.Museum['name'] == payload['name'])

			return jsonify (
				data={},
				message=f'{payload["name"]} is already registered',
				status=401
			), 401

		except models.DoesNotExist:

			created_museum = models.Museum.create(
				name=payload['name'],
				email=payload['email'],
				password=generate_password_hash(payload['password'])
			)

			login_user(created_museum)

			created_museum_dict = model_to_dict(created_museum)
			created_museum_dict.pop('password')
			print(created_museum_dict)
			return jsonify (
				data=created_museum_dict,
				message=f'successfully created {created_museum_dict["name"]}',
				status=201
			), 201


	#print('request in register', request.get_json())


	return "check terminal"