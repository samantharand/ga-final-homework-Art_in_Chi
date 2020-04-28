import models

from flask import Blueprint

museum = Blueprint('museum', 'museum')

# test route
@museum.route('/', methods=['GET'])
def test():
	return 'yayyyy museum test route works'