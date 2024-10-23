from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de inscritos
inscritos = []

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obtener los datos del formulario
        fecha = request.form['fecha']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        turno = request.form['turno']
        seminarios = request.form.getlist('seminario')
        
        # Crear un nuevo registro y añadirlo a la lista
        inscrito = {
            'fecha': fecha,
            'nombre': nombre,
            'apellidos': apellidos,
            'turno': turno,
            'seminarios': '; '.join(seminarios)
        }
        inscritos.append(inscrito)
        
        return redirect(url_for('listado'))
    
    return render_template('registro.html')

@app.route('/listado')
def listado():
    return render_template('listado.html', inscritos=inscritos)

@app.route('/editar/<int:indice>', methods=['GET', 'POST'])
def editar(indice):
    inscrito = inscritos[indice]
    if request.method == 'POST':
        # Actualizar el registro existente
        inscrito['fecha'] = request.form['fecha']
        inscrito['nombre'] = request.form['nombre']
        inscrito['apellidos'] = request.form['apellidos']
        inscrito['turno'] = request.form['turno']
        inscrito['seminarios'] = '; '.join(request.form.getlist('seminario'))
        return redirect(url_for('listado'))
    
    return render_template('editar.html', inscrito=inscrito)

@app.route('/eliminar/<int:indice>')
def eliminar(indice):
    # Eliminar el inscrito de la lista
    del inscritos[indice]
    return redirect(url_for('listado'))

if __name__ == '__main__':
    app.run(debug=True)