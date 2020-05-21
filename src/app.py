from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from usuarioDAO import Usuario
from productoDAO import Producto
user = Usuario()
producto = Producto()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def listar():
    return jsonify({'mensaje': 'Bienvenidos a Flask'})


@app.route('/usuario/listar', methods=['GET'])
def users():
    try:
        rows = user.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)


@app.route('/usuario/crear', methods=['POST'])
def agregarusuario():
    try:
        _json = request.json
        user.nomuser=_json['nomuser']
        user.clave=_json['pass']
        print(user.clave,user.nomuser)
        if request.method=='POST':
            resp=user.agregarusuario()
            resp=jsonify('USUARIO')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)

@app.route('/usuario/eliminar/<int:id>', methods=['GET'])
def eliminarusuario(id):
    try:
        user.idusuario=id
        resp=user.delete()
        resp=jsonify('Usuario Eliminado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)    
@app.route('/usuario/modificar', methods=['PUT'])
def modificarusuario():
    try:
        _json=request.json
        user.nomuser=_json['nomuser']
        user.clave=_json['pass']
        user.idusuario=_json['iduser']
        if request.method == 'PUT':
            resp = user.modificarusuario()
            resp = jsonify('Usuario Modificado')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)



@app.route('/producto/listar', methods=['GET'])
def productos():
    try:
        rows = producto.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)


@app.route('/producto/crear', methods=['POST'])
def agregarproducto():
    try:
        _json = request.json
        producto.nomproducto=_json['nomproducto']
        producto.precio=_json['precio']
        producto.cantidad=_json['cantidad']
        if request.method=='POST':
            resp=producto.agregarproducto()
            resp=jsonify('PRODUCTO')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)
        
@app.route('/producto/eliminar/<int:id>', methods=['GET'])
def eliminarproducto(id):
    try:
        producto.idproducto=id
        resp=producto.delete()
        resp=jsonify('Producto Eliminado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)  

@app.route('/producto/modificar', methods=['PUT'])
def modificarproducto():
    try:
        _json=request.json
        producto.precio=_json['precio']
        producto.cantidad=_json['cantidad']
        producto.nomproducto=_json['nomproduc']
        producto.idproducto=_json['idproduc']
        if request.method == 'PUT':
            resp = producto.modificarproducto()
            resp = jsonify('Usuario Modificado')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)    