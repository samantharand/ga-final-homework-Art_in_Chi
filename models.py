from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('art.sqlite')

class Museum(UserMixin, Model):
	name = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField()

	class Meta:
		database = DATABASE

class Art(Model):
	name = CharField()
	artist = CharField()
	year_made = IntegerField()
	current_residence = ForeignKeyField(Museum, backref='art')

	class Meta:
		database = DATABASE

def init():
	DATABASE.connect()
	DATABASE.create_tables([Museum, Art], safe=True)
	print('Art DB Connected')
	DATABASE.close()