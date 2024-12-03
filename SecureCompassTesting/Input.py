[CODEBLOCK]
from flask import Flask, request
import sqlite3
from flask_wtf.csrf import CSRFProtect

app = Flask(name)
app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)

@app.route('/search')
def search():
query = request.args.get('query', '')
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM users WHERE name = '{query}'")
results = cursor.fetchall()
return str(results)

if name == 'main':
app.run(debug=True)
[/CODEBLOCK
