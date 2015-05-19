# backbone-flask-notes
A simple CRUD application for Notes created in backbonejs and flask

#Installation#

-pip install flask
-pip install flask-mysql
-Create a database in mysql
-Execute notes.sql in notes database
-Modify server.py and change following configuration based on your requirements
	app.config['MYSQL_DATABASE_USER'] = 'user'
	app.config['MYSQL_DATABASE_PASSWORD'] = 'pass'
	app.config['MYSQL_DATABASE_DB'] = 'notes'
	app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#Run Server#

-python server.py

Server is now running http://localhsot:5000

#Specifications#

GET http://localhost:5000/notes - get all notes
POST http://localhost:5000/notes - create a note
PUT http://localhost:5000/note/:id - update a note with given id
DELETE http://localhost:5000/note/:id - delete a note with given id