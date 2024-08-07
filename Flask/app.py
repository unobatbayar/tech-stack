from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", name = request.args.get("name", "world"))

@app.route("/greet")
def greet():
    return render_template("greet.html", name = request.args.get("name", "world"))