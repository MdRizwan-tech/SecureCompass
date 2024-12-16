from flask import Flask, request, jsonify
import logging

app = Flask(name)

logging.basicConfig(filename='app.log', level=logging.ERROR)

@app.route('/submit', methods=['POST'])
def submit():
	try:
		data = request.json
		user_input = data['user_input']
		# Vulnerable to XSS
		return f"

{user_input}

"
	except Exception as e:
		logging.error('Error occurred: %s', e)
		return jsonify({'error': 'An error occurred, please try again later.'}), 500

if __name__ == '__main__':
	app.run(debug=False)