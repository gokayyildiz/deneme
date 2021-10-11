from flask import Flask, render_template, request, redirect, url_for, session,  Response
from flask import jsonify
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/onur")
def onur():
    return render_template("deneme.html")



if __name__=='__main__':
    app.run(debug=True)