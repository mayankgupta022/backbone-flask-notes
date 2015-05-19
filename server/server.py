from flask import Flask, request
from flaskext.mysql import MySQL
from cors import *
import json

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass'
app.config['MYSQL_DATABASE_DB'] = 'notes'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

def log(msg):
	log_file = open('log.txt', 'a')
	log_file.write(msg + '\n')
	log_file.close()

@app.route('/notes', methods=['GET', 'POST'])
@crossdomain(origin='*')
def notes():
	con = mysql.connect()
	cursor = con.cursor()
	info = dict()

	if request.method == 'GET':
		stmt = "SELECT * FROM notes"
		cursor.execute(stmt)
		data = cursor.fetchall()		
		info = [{"id" : item[0], "title": item[1], "content": item[2]} for item in data]

	else:
		title = request.form['title']
		content = request.form['content']
		stmt = "INSERT INTO notes (title, content) VALUES (%s, %s)"
		data = (title, content)
		cursor.execute(stmt, data)
		id = cursor.lastrowid
		con.commit()
		info = {"id" : id, "title": title, "content": content}

	return json.dumps(info)

@app.route('/note/<int:id>', methods=['PUT', 'DELETE'])
@crossdomain(origin='*')
def note(id):
	con = mysql.connect()
	cursor = con.cursor()
	info = dict()

	if request.method == 'PUT':
		title = request.form['title']
		content = request.form['content']
		stmt = "UPDATE notes SET title = %s , content = %s WHERE id = %s"
		data = (title, content,id)
		cursor.execute(stmt, data)
		log(str(id))
		con.commit()
		info = {"id" : id, "title": title, "content": content}

	else:
		stmt = "DELETE FROM notes WHERE id = %s"
		data = (id)
		cursor.execute(stmt, data)
		con.commit()
		info = {"id" : id}

	return json.dumps(info)

# @app.errorhandler(404)
# def page_not_found(e):
# 	"""Return a custom 404 error."""
# 	return 'Sorry, Nothing at this URL.', 404


# @app.errorhandler(500)
# def application_error(e):
# 	"""Return a custom 500 error."""
# 	return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == "__main__":
	app.run()
