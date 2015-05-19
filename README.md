backbone-flask-notes
====================

A simple CRUD application for Notes created in backbonejs and flask

Installation
------------

1. <pre class="console">pip install flask</pre>
2. <pre class="console">pip install flask-mysql</pre>
3. Create a database in mysql
4. Execute notes.sql in notes database
5. Modify server.py and change following configuration based on your requirements
	<pre class="console">
	app.config['MYSQL_DATABASE_USER'] = 'user'
	app.config['MYSQL_DATABASE_PASSWORD'] = 'pass'
	app.config['MYSQL_DATABASE_DB'] = 'notes'
	app.config['MYSQL_DATABASE_HOST'] = 'localhost'
	</pre>

Run Server
----------

<pre class="console">python server.py</pre>

Server is now running `http://localhsot:5000`

Specifications
--------------

1. GET `http://localhost:5000/notes` - get all notes
2. POST `http://localhost:5000/notes` - create a note
3. PUT `http://localhost:5000/note/:id` - update a note with given id
4. DELETE `http://localhost:5000/note/:id` - delete a note with given id