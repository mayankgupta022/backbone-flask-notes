from flask import Flask, request, Response
from flaskext.mysql import MySQL
from flask.ext.cors import CORS
import json

mysql = MySQL()
app = Flask(__name__)
cors = CORS(app)

app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass'
app.config['MYSQL_DATABASE_DB'] = 'notes'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

def log(msg):
	log_file = open('log.txt', 'a')
	log_file.write(msg + '\n')
	log_file.close()

@app.route('/notes', methods=['GET', 'POST', 'OPTIONS'])
def notes():
	params  = json.loads(json.dumps(request.json))

	con = mysql.connect()
	cursor = con.cursor()
	info = dict()

	if request.method == 'GET':
		stmt = "SELECT * FROM notes"
		cursor.execute(stmt)
		data = cursor.fetchall()		
		info = [{"id" : item[0], "title": item[1], "description": item[2]} for item in data]

	elif request.method == 'POST':
		title = params['title']
		description = params['description']
		stmt = "INSERT INTO notes (title, description) VALUES (%s, %s)"
		data = (title, description)
		cursor.execute(stmt, data)
		id = cursor.lastrowid
		con.commit()
		info = {"id" : id, "title": title, "description": description}

	return Response(json.dumps(info),  mimetype='application/json')

@app.route('/note/<int:id>', methods=['GET', 'PUT', 'DELETE', 'OPTIONS'])
def note(id):
	params  = json.loads(json.dumps(request.json))

	con = mysql.connect()
	cursor = con.cursor()
	info = dict()

	if request.method == 'GET':
		stmt = "SELECT * FROM notes WHERE id = %s"
		data = (id)
		cursor.execute(stmt, data)
		data = cursor.fetchone()
		info = {"id" : data[0], "title": data[1], "description": data[2]}		

	elif request.method == 'PUT':
		title = params['title']
		description = params['description']
		stmt = "UPDATE notes SET title = %s , description = %s WHERE id = %s"

		data = (title, description,id)
		cursor.execute(stmt, data)
		con.commit()
		info = {"id" : id, "title": title, "description": description}

	elif request.method == 'DELETE':
		stmt = "DELETE FROM notes WHERE id = %s"
		data = (id)
		cursor.execute(stmt, data)
		con.commit()
		info = {"id" : id}

	return Response(json.dumps(info),  mimetype='application/json')

# @app.errorhandler(404)
# def page_not_found(e):
# 	"""Return a custom 404 error."""
# 	return 'Sorry, Nothing at this URL.', 404


# @app.errorhandler(500)
# def application_error(e):
# 	"""Return a custom 500 error."""
# 	return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == "__main__":
	# import logging
	# logging.basicConfig(filename='error.log',level=logging.DEBUG)
	app.debug=True
	app.run()
