from flask import Flask, render_template, request, redirect, url_for, session,  Response
from flask import jsonify
import requests

application = Flask(__name__)

@application.route("/")
def hello_world():
    return "Hello World"

@application.route("/onur")
def onur():
    return render_template("deneme.html")



if __name__=='__main__':
    application.run(debug=True)