from flask import Flask, request, jsonify
from models import db, Item
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/items", methods=["POST"])
def create_item():
    name = request.form.get("name")
    description = request.form.get("description")

    item = Item(name=name, description=description)
    db.session.add(item)
    db.session.commit()

    return jsonify({"message": "Item created", "id": item.id}), 201


@app.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([
        {"id": item.id, "name": item.name, "description": item.description, "created_at": item.created_at}
        for item in items
    ])

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify({"id": item.id, "name": item.name, "description": item.description})

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.get_json()
    item.name = data["name"]
    item.description = data.get("description")
    db.session.commit()
    return jsonify({"message": "Item updated"})

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted"})
