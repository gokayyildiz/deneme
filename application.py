from flask import Flask, render_template


application = Flask(__name__)



@application.route("/")
def odur():
    return render_template("deneme.html")



if __name__=='__main__':
    application.run()