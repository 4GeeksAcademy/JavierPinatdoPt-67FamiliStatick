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

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

John = {
    "first_name" : "John",
    "last_name" : jackson_family.last_name,
    "age" : 33,
    "lucky_numbers" : [7, 13, 22]
}       

Jane = {
    "first_name" : "Jane",
    "last_name" : jackson_family.last_name,
    "age" : 35,
    "lucky_numbers" : [10, 14, 3]
}      

Jimmy = {
    "first_name" : "John",
    "last_name" : jackson_family.last_name,
    "age" : 33,
    "lucky_numbers" : [1],
}  

jackson_family.add_member(John)
jackson_family.add_member(Jane)
jackson_family.add_member(Jimmy)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }
    #endpoint traer miembro
    @app.route('/member', methods=['POST'])
    def add_member():
    # Obtener los datos del miembro del cuerpo de la solicitud
        member_data = request.json

        if not member_data:
            return jsonify({"error": "Faltan datos del miembro"}), 400

    # Endpoint añadir un miembro
    try:
        jackson_family.add_member(member_data)
        return jsonify({"message": "Miembro añadido correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    #endpoiunt delete
    @app.route('/member/<int:member_id>', methods=['DELETE'])
    def delete_member(member_id):
    # Intentar eliminar el miembro usando el método delete_member de jackson_family
        success = jackson_family.delete_member(member_id)

    if success:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Miembro no encontrado"}), 404
    
    #endpoint  traer todos los mimebros
    @app.route('/members', methods=['GET'])
    def get_all_members():
    # Obtener todos los miembros usando el método get_all_members de jackson_family
        members = jackson_family.get_all_members()
    
    return jsonify(members), 200






    return jsonify(response_body), 200






# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
