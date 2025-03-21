from flask import Flask, render_template, redirect, url_for
from producto import Producto
from flask import request 
from flask import Response

app = Flask(__name__)
productos = [Producto("Computadora",200),Producto("celular",130)]
@app.route('/')
def index():
    
    return render_template('productos.html',productos=productos)

@app.route('/editar/<producto>/<precio>')
def editar(producto,precio):
    print(producto)
    return render_template('editar.html',producto=producto,precio=precio)
    
@app.route('/guardar', methods=['POST'])
def guardar():
    n= request.form.get('nombre')
    p= request.form.get('precio')
    p = int(p)
    print (n,p)
    i=0
    for e in productos:
        if e.nombre == n:
            e.precio = p
            break
    return redirect('/')
            #productos[i] = Producto(n,p)
           # print(f"{e.nombre} {e.precio}")
       # i+=1
    #return Response("guardado", headers={'Location': '/'}, status=302)

@app.route('/eliminar/<nombre>', methods=['GET'])
def eliminar(nombre):
    global productos  # Asegura acceso a la variable global
    i = 0
    for e in productos:
        if e.nombre == nombre:
            productos.pop(i)
            print(f"{e.nombre} eliminado con precio {e.precio}")
            break  # Salir del bucle después de eliminar
        i += 1
    return Response("eliminado", headers={'location': '/'}, status=302)

@app.route('/crear', methods=['POST'])
def crear():
    n = request.form.get('nombre')
    p = int(request.form.get('precio'))
    productos.append(Producto(n, p))
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)