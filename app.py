import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Jake Mooradian in 3308'
    
@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://render_example_vh4x_user:3sJyc4p7eglZ6JCiH6wMAWihsqNqVLD6@dpg-d7a4m1npm1nc73btehhg-a/render_example_vh4x")
    conn.close()
    return "Database Connection Successful"