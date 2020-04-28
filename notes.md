April 28 Notes  - order of operations

--- Adding User Auth n Stufffff ---



	pip3 install flask-login flask-bcrypt

	pip3 freeze > requirements.txt

Import into Models.py to build user model
	- Do all the user model set up 
	- Change art current res value to foreign key
	- IN TERMINAL - can move old db into new folder to archive
		# mv art.sqlite art.sqlite.no-relation
		# can check relation in sqlite ---- run .schema art

Run in CLI
	
	python3 app.py

Stop python3 app.py, check squlite

	sqlite3 art.sqlite
	.tables
	.schema user 		--> basically shows the code that created it ?


Create and configure a login manager in app.py
	Run python app to see if theres any initial errors

Create `users.py` in `resources` dir





















