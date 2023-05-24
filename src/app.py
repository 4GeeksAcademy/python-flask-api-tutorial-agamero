from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [{"label": "My first task", "done": False}]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)  # Convierte la lista 'todos' a formato JSON
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json  # Obtiene el contenido del cuerpo de la solicitud en formato JSON
    todos.append(request_body)  # Añade el nuevo todo a la lista 'todos'
    return jsonify(todos)  # Devuelve la lista 'todos' actualizada como respuesta en formato JSON


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):  # Verifica si la posición es válida dentro del rango de índices de la lista 'todos'
        del todos[position]  # Elimina la tarea de la lista 'todos' en la posición dada
        return jsonify(todos)  # Devuelve la lista 'todos' actualizada como respuesta en formato JSON
    else:
        return jsonify({"error": "Invalid position"})  # Devuelve un mensaje de error en formato JSON si la posición es inválida


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
