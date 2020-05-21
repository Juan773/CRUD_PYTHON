import pymysql
from conexion import Conexion
from sqlalchemy import create_engine
from json import dumps
cx = Conexion()

class Producto:
    idproducto = 0
    nomproducto = ""
    precio = 0
    cantidad = 0
    estado = ""
    def readAll(self):
        try:
            conexion=cx.conecta()
            cursor = conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('listar_producto')
            rows = cursor.fetchall()
            print(rows)
            return rows
        except Exception as e:
            print(e)
        finally:
            conexion.close()
    def delete(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('delete_producto',[self.idproducto])
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def agregarproducto(self):
        nomproducto=self.nomproducto
        precio=self.precio
        cantidad=self.cantidad
        data=[nomproducto,precio,cantidad]
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("create_producto",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def buscarproductos(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('read_producto',[self.idproducto,])
            rows=cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def modificarproducto(self):
        try:
            nomproducto=self.nomproducto
            precio=self.precio
            cantidad=self.cantidad
            idp=self.idproducto
            data=[nomproducto,precio,cantidad,idp]
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("update_producto",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()