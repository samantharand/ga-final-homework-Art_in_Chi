import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, current_user, logout_user

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
		models.Museum.get(models.Museum.email == payload['email'])
		
		return jsonify(
			data={},
			message=f'email {payload["email"]} is already registered',
			status=401
		), 401
	
	except models.DoesNotExist:

		try:
			# name of museum
			models.Museum.get(models.Museum.name == payload['name'])

			return jsonify(
				data={},
				message=f'username {payload["name"]} is already registered',
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
			print('CREATED_MUSEUM_dict',created_museum_dict)
			created_museum_dict.pop('password')
			print(created_museum_dict)
			return jsonify(
				data=created_museum_dict,
				message=f'successfully created {created_museum_dict["name"]}',
				status=201
			), 201

# login
@museum.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	#payload['name'] = payload['name'].lower()
	print("PAYLOAD line 68", payload)
	try:

		museum = models.Museum.get(models.Museum.email == payload['email'])

		museum_dict = model_to_dict(museum)
		print('MUSEUM_DICT line 74',museum_dict)
		password_is_good = check_password_hash(museum_dict['password'], payload['password'])


		if password_is_good:
			login_user(museum)
			print('CURRENT USER', current_user) # THIS WORKS ??? 
			# print('LOGIN USER', login_user(museum)) 
			#print('user should be logged in???')
			museum_dict.pop('password')

			return jsonify(
				data=museum_dict,
				message=f"successfully logged into {museum_dict['name']}'s account",
				status=200
			), 200
		else:
			print('bad password bro')

			return jsonify(
				data={},
				message=f"email or password incorrect :(",
				status=401
			), 401	
	except models.DoesNotExist:
		print('username doesnt exist, dummy')

		return jsonify(
			data={},
			message=f'email or password incorrect :(',
			status=401
		), 401

	return "checka da termeenal"

# logout
@museum.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return jsonify(
		data={},
		message="successfully logged out :)",
		status=200
	), 200

#templ route
@museum.route('/all', methods=['GET'])
def museum_index():
	museums = models.Museum.select()
	museum_dicts = [ model_to_dict(museum) for museum in museums ]

	for museum_dict in museum_dicts:
		museum_dict.pop('password')
	print('CURRENT USER LINE 127', current_user)
	return jsonify(museum_dicts)

#temp route
@museum.route('/current', methods=['GET'])
def get_current_museum():
	print(current_user)
	print(type(current_user))

	museum_dict = model_to_dict(current_user)
	print(museum_dict);

	if not current_user.is_authenticated:
		return jsonify(
			data={},
			message="no user is currently logged in",
			status=401
		), 401

	else: 
		museum_dict = model_to_dict(current_user)
		museum_dict.pop('password')

		return museum_dict



	return "cehck term"













