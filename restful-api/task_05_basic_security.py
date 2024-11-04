from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from datetime import timedelta
from flask_jwt_extended import (
        JWTManager, create_access_token, jwt_required, get_jwt_identity
        )


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
        "user1": {
            "username": "user1",
            "password": generate_password_hash("password"),
            "role": "user"
            },
        "admin1": {
            "username": "admin1",
            "password": generate_password_hash("password"),
            "role": "admin"
            }
        }


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@jwt.unauthorized_loader
def unauthorized_err(err):
    return jsonify({"error": "Token faltante o inválido"}), 401


@jwt.invalid_token_loader
def invalid_token_err(err):
    return jsonify({"error": "Token inválido"}), 401


@jwt.expired_token_loader
def expired_token_err(err):
    return jsonify({"error": "El token ha expirado"}), 401


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Faltan el nombre de usuario o la contraseña"}), 400


    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_tkn = create_access_token(
            identity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_tkn)


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Se requiere acceso de administrador"}), 403
    return jsonify(message="Acceso de Administrador: Concedido")


if __name__ == '__main__':
    app.run()
