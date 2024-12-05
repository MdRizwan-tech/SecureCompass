import os
from flask import Flask, request

app = Flask(name)
csrf = CSRFProtect(app)

@app.route('/ping', methods=['GET'])
def ping():
	target = request.args.get('target', 'localhost')
	result = os.popen(f"ping -c 1 {target}").read() # Vulnerable to command injection.
	return f"

{result}
"
if name == 'main':
	app.run(debug=True)
