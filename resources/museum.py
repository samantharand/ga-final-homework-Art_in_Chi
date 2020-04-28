import models

from flask import Blueprint, request

museum = Blueprint('museum', 'museum')

# test route
@museum.route('/', methods=['GET'])
def test():
	return 'yayyyy museum test route works'

# register your museum
@museum.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	# see if the user exists
	print('pre-lower', payload)
	payload['name'] = payload['name'].lower()
	payload['email'] = payload['email'].lower()
	print('post-lower', payload)
    # if so -- we don't want to create the user

    # response: "user with that email already exists"

	# if the user does not exist

    # create them

    # respond with new object and success message


	#print('request in register', request.get_json())
	


	return "check terminal"