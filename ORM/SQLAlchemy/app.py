from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# SQLite database URI (relative path)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    Username = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    Password = db.Column(db.String(255), nullable=False)

# Create the tables (ensure this is inside the app context)
with app.app_context():
    db.create_all()  # Create all tables if they don't exist

# Simple route to check if the app is running
@app.route('/')
def index():
    return 'Flask app is running!'

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
