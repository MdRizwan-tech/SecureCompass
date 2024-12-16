from flask import Flask, request, jsonify
import sqlite3
import logging

app = Flask(name)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

@app.route('/submit', methods=['POST'])
def submit():
	try:
		data = request.json
		user_id = data['user_id']
		conn = sqlite3.connect('database.db')
		cursor = conn.cursor()
		# Fixed SQL Injection vulnerability
		cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
		result = cursor.fetchall()
		return jsonify(result)
	except Exception as e:
		logging.error('Error occurred: %s', e)
		return jsonify({'error': 'An error occurred, please try again later.'}), 500

if name == 'main':
	app.run(debug=False)