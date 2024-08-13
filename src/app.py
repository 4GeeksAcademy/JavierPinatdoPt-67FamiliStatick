"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")



# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Traer todos los miembros
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Traer un solo miembro
@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member: 
        return jsonify(member), 200
    else:
        return jsonify({"msg":"miembro no encontrado"}), 404
    
# Añadir miembro 
@app.route('/member', methods=['POST'])
def add_member():
    body= request.get_json()
    if not body or not "first_name" in body or not "age" in body or not "lucky_numbers" in body:
        return jsonify({"msg":"falta dato por entrar"}), 400
    new_member = {
        "id": jackson_family._generateId(),
        "first_name": body["first_name"],
        "last_name": jackson_family.last_name,
        "age": body ["age"],
        "lucky_numbers": body ["lucky_numbers"],
    }
    jackson_family.add_member(new_member)
    return jsonify(new_member), 201

 # Eliminar miembro   
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    member= jackson_family.delete_member(id)
    if member: 
        return jsonify({"msg":"miembro eliminado", "member":member}), 200
    else:
        return jsonify({"msg":"miembro no encontrado"}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
