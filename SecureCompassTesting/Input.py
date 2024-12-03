from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{query}'")
    results = cursor.fetchall()
    return str(results)

if __name__ == '__main__':
    app.run(debug=True)
