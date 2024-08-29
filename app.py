from flask import Flask, request, jsonify
from fastapi.encoders import jsonable_encoder

app = Flask(__name__)

todolist = [
    {
        "id": 1,
        "task": "clean my room"
    }
]

@app.get("/")
def root():
    return {"todolist": todolist}

@app.post("/todo")
def create_todo():
    request_data = request.get_json()
    new_todo = {
        "id": request_data["id"],
        "task": request_data["task"]
    }
    todolist.append(new_todo)
    return new_todo, 201


@app.put("/todo")
def update_todo():
    update_item_encoded = jsonable_encoder('id')
    items[item_id] = update_item_encoded
    return update_item_encoded


@app.delete("/todo")
def delete_todo():
    request_data = request.get_json()
    todo_id = request_data.get("id")

    global todolist
    todolist = [item for item in todolist if item["id"] != todo_id]

    return {"message": f"Todo item with id {todo_id} deleted"}, 200


