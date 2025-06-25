from cs50 import SQL
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
  

sports = [ "Basketball", "Soccer", "Ultimate Frisbee"]


@app.route("/")
def index():
    return render_template("index.html", sports=sports)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")

    if not name:
        return render_template("error.html", error_message="No name found")
    sport = request.form.get("sport")
    if sport not in sports:
        return render_template("error.html", error_message="No sport found")

    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)

    return render_template("success.html")

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT name, sport FROM registrants")
    return render_template("registrants.html", registrants=registrants)

# Define a route
@app.route('/weather')
def weather():
    # Create a Python dictionary with weather data
    weather_data = {
        'city': 'Tokyo',
        'temperature': 22,
        'unit': 'Celsius',
        'condition': 'Clear'
    }
    
    # Return the dictionary as a JSON response
    return jsonify(weather_data)