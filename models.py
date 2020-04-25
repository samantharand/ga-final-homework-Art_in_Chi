from peewee import *

DATABASE = SqliteDatabase('art.sqlite')

class Art(Model):
	name = CharField()
	artist = CharField()
	current_residence = CharField()

	class Meta:
		database = DATABASE

def init():
	DATABASE.connect()
	DATABASE.create_tables([Art], safe=True)
	print('Art DB Connected')
	DATABASE.close()