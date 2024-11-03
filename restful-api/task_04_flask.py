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
    username_list = []

    for iter_dict in dictionary_usr:
        username_list.append(iter_dict)

    return jsonify(username_list)


@app.route('/status')
def okay_status():
    return jsonify({"Status": "OK"})


@app.route('/users/<username>')
def username_funct(username):
    if username in dictionary_usr:
        return jsonify(dictionary_usr[username])

    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def Post_req():
    data = request.get_json()
    username = data['username']
    dictionary_usr[username] = {
            "name": data['name'],
            "age": data['age'],
            "city": data["city"]
            }


return jsonify({"message": "User added successfully!",
                "user": dictionary_usr[username]})


if __name__ == "__main__":
    app.run(debug=True)
