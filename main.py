from flask import Flask, send_file, send_from_directory
import mimetypes

app = Flask(__name__)


@app.route('/home')
def homepage():
    return "This is homepage. Please go to webpage  /static/python_repos.py to see the graph."








