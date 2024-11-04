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


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(
                identity={"username": username, "role": user['role']})
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Credenciales inválidas"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(message="JWT Auth: Access Granted", user=current_user)


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Se requiere acceso de administrador"}), 403
    return jsonify(message="Acceso de Administrador: Concedido")


@jwt.unauthorized_loader
def unauthorized_err(err):
    return jsonify({"error": "Token faltante o inválido"}), 401


@jwt.invalid_token_loader
def invalid_token_err(err):
    return jsonify({"error": "Token inválido"}), 401


@jwt.expired_token_loader
def expired_token_err(err):
    return jsonify({"error": "El token ha expirado"}), 401


@jwt.revoked_token_loader
def revoked_tkn_error(err):
    return jsonify({"error": "El token ha sido revocado"}), 401


@jwt.needs_fresh_token_loader
def needs_fresh_token_error(err):
    return jsonify({"error": "Se requiere un token fresco"}), 401


if __name__ == '__main__':
    app.run()
