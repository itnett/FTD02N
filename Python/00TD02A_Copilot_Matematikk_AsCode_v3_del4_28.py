python
from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(dbname="testdb", user="user", password="password", host="localhost")
    return conn

@app.route('/metrics', methods=['GET'])
def get_metrics():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM PerformanceMetrics;')
    metrics = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(debug=True)