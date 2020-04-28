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
	print('request in register', request.get_json())
	return "check terminal"