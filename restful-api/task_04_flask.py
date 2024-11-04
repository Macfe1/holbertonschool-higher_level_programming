from flask import Flask, jsonify, request

app = Flask(__name__)

dictionary_usr = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def usernames():
    if not dictionary_usr:
        return jsonify([])
    username_list = list(dictionary_usr.keys())
    return jsonify(username_list)


@app.route('/status')
def okay_status():
    return "OK"


@app.route('/users/<username>')
def username_funct(username):

    usern = dictionary_usr.get(username)
    
    if usern:
        return jsonify(usern)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def post_req():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data.get('username')

    if username in dictionary_usr:
        return jsonify({"error": "Username already exists"}), 400

    user_data = {
            "username": username,
            "name": data.get("name", ""),
            "age": data.get("age", 0),
            "city": data.get("city", "")
            }
    dictionary_usr[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data,
        }), 201


if __name__ == "__main__":
    app.run(port=5000)
