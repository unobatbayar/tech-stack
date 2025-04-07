from flask import Flask, render_template, request

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
  
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if name and sport:
        return render_template("success.html")
    return render_template("failure.html")