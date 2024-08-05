import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Josiah Panak in 3308.'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://panakj:RoDM2DMDouqUI5GL3JgWar0JlE2Mu11z@dpg-cqoblgtds78s73bu35s0-a/flask_lab_10_db")
    conn.close()
    return "Database Connection Successful."
