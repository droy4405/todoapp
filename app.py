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




