from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        # No CSRF protection
        return 'Form submitted successfully'
    except Exception as e:
        logging.error('Error occurred: %s', e)
        return jsonify({'error': 'An error occurred, please try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=False)