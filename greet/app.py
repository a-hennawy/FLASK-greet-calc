from flask import Flask
app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return """
        <h1> welcome </h1>"""


@app.route('/welcome/home')
def home():
    return """
        <h1> welcome home </h1>"""


@app.route('/welcome/back')
def back():
    return """
        <h1> welcome back </h1>"""
