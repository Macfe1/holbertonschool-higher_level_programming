from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask API!"


dictionary_usr = {
        "macfe": {"name": "Mafe", "age": 23, "city": "Bogota"},
        "pablo": {"name": "Pablo", "age": 20, "city": "Los Angeles"}
        }


@app.route('/data')
def usermames():
    for iter_dict in dictionary_usr:
        username_list.append(iter_dict)

    return jsonify(username_list)


@app.route('/status')
def okay_status():
    return "OK"


@app.route('/users/<username>')
def username_funct(username):
    if username in dictionary_usr:
        return jsonify(dictionary_usr[username])

    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def Post_req():
    data = request.get_json()
    username = data.get('username')
    
    if username is None:
        return jsonify({"error": "Username is required"}), 400

    if username in dictionary_usr:
        return jsonify({"error": "The user already exists"}), 400

    dictionary_usr[username] = {
            "name": data.get('name'),
            "age": data.get('age'),
            "city": data.get('city')
            }

    return jsonify({
        "message": "User added successfully!",
        "user": {
            "username": username,
            "name": data.get('name'),
            "age": data.get('age'),
            "city": data.get('city')
            }
        }), 201


if __name__ == "__main__":
    app.run(port=5000)
