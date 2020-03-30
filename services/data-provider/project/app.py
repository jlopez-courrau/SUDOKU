"""
TODO: add docstring
"""
from flask import Flask, jsonify

app = Flask(__name__)
# app.config.from_object("project.config.Config")
# db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    """"
    TODO: this function is just a hello world for testing
    """
    return jsonify(message="Hello from Data provider")

