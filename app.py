from flask import Flask, request, jsonify
import storage
import logic
from datetime import timedelta

app = Flask(__name__)
storage.init()

@app.get("/films")
def list_films():
    category = request.args.get("category")       # ?category=scifi або None
    return jsonify(storage.load(category))

@app.post("/films")
def add_item():
    data = request.get_json(silent=True)
    try:
        duration = data['duration']
        hours, minutes, seconds = duration.split(',')
        duration = timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
        data['duration'] = duration
    except (IndexError, ValueError) as e:
        return jsonify({"error": "duration повинен мати вигляд ГОДИНИ,ХВИЛИНИ,СЕКУНДИ"}), 404
    new_id = logic.add(data)
    return jsonify({"id": new_id}), 201

@app.delete("/films/<int:item_id>")
def delete_item(item_id):
    if logic.remove_record(item_id):
        return jsonify({"deleted": item_id})
    return jsonify({"error": "не знайдено"}), 404

@app.get("/report")
def report():
    return jsonify(logic.films_by_category())

if __name__ == "__main__":
    app.run(debug=True)