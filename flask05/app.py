from flask import Flask, render_template, redirect, url_for
from producto import Producto
from flask import request 
from flask import Response
import sqlite3


app = Flask(__name__)
#productos = [Producto("Computadora",200),Producto("celular",130)]
@app.route('/')
def index():
    con =conexion()
    productos = con.execute('select*from productos').fetchall()
    con.close()
    return render_template('productos.html',productos=productos)

@app.route('/editar/<id>')
def editar(id):
    con = conexion()
    p = con.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    con.close()
   
    return render_template('editar.html',producto=p)
    
@app.route('/guardar', methods=['POST'])
def guardar():
    n= request.form.get('nombre')
    p= request.form.get('precio')
    id = request.form.get('id')
    print(f"{n} {p} {id}")
    con = conexion()
    con.execute("update productos set nombre=?, precio=? where id=?",(n,p,id))
    con.commit()
    con.close()
    #p = int(p)
   # print (n,p)
    #i=0
    #for e in productos:
        #if e.nombre == n:
           # e.precio = p
            #break
    #return redirect('/')
            #productos[i] = Producto(n,p)
           # print(f"{e.nombre} {e.precio}")
       # i+=1
    return Response("guardado", headers={'Location': '/'}, status=302)

@app.route('/eliminar/<id>')
def eliminar(id):
    con = conexion()
    con.execute("delete from productos where id=?",(id))
    con.commit()
    con.close()
   # global productos  # Asegura acceso a la variable global
   # i = 0
    #for e in productos:
     #   if e.nombre == nombre:
      #      productos.pop(i)
       #     print(f"{e.nombre} eliminado con precio {e.precio}")
        #    break  # Salir del bucle después de eliminar
        #i += 1
    return Response("eliminado", headers={'location': '/'}, status=302)

@app.route('/crear', methods=['POST'])
def crear():
    n = request.form.get('nombre')
    p = int(request.form.get('precio'))
    #productos.append(Producto(n, p))
    con = conexion()
    con.execute('insert into productos (nombre , precio) values (?,?)',(n,p))
    con.commit()
    con.close()
    return redirect(url_for('index'))

def conexion():
    con = sqlite3.connect('basedatos.db')
    con.row_factory = sqlite3.Row
    return con

def iniciar_db():
    con = conexion()
    con.execute('''
        CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        PRECIO REAL NOT NULL
        )
    ''')
    con.commit()
    con.close()

if __name__=='__main__':
    iniciar_db()
    app.run(host='0.0.0.0', debug=True)