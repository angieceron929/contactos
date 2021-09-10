from flask import Flask,request,render_template,redirect,session,url_for,flash
from contactos import RegistroCont

app = Flask(__name__)
app.secret_key ='spbYO0JJ0PUFLUikKYbKrpS5w3KUEnab5KcYDdYb'



@app.route('/',methods=['GET'])
def index():
    if request.method == 'GET':
        contactos = RegistroCont()
        contactos = contactos.Listado()
        return render_template('index.html',contactos = contactos, active=['active',''])
    
@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'GET':
      return render_template('/usuarios/crear.html',active=['','active'])
    if request.method == 'POST':
      iden = request.form.get('identificacion')
      nombre = request.form.get('nombres')
      apellidos = request.form.get('apellidos')
      email = request.form.get('email')
      celular = request.form.get('celular')
      
      new_cont = RegistroCont()
      new_cont =new_cont.insertarCont(iden,nombre,apellidos,email,celular)
      flash("El contacto ha sido añadido con exito","badge bg-success")
      return redirect(url_for('index'))

    return render_template(url_for('index'))

@app.route('/contact/edit', methods=['POST'])  
def contact_edit():
    if request.method == 'GET':
        return redirect(url_for('index'))
    if request.method == 'POST':

      id = request.form.get('id')

      contacto = RegistroCont()
      contacto = contacto.EditarCont(id)
   
      return render_template('/usuarios/editar.html',contacto =contacto,active=['',''])

@app.route('/contact/update', methods=['GET', 'POST'])  
def contact_update():
   if request.method == 'GET':
         return redirect(url_for('index'))
   if request.method == 'POST':
         id = request.form.get('identificador')
         iden = request.form.get('identificacion')
         nombre = request.form.get('nombres')
         apellidos = request.form.get('apellidos')
         email = request.form.get('email')
         celular = request.form.get('celular')

         edit_cont = RegistroCont()
         edit_cont =edit_cont.ActualizarCont(iden,nombre,apellidos,email,celular,id)
         flash("El contacto ha sido editado","badge bg-success")
         return redirect(url_for('index'))

@app.route('/contact/delete', methods=['GET', 'POST'])  
def delete_contact():
   if request.method == 'GET':
       return redirect(url_for('index'))

   if request.method == 'POST':
      id = request.form.get('id')
      contacto = RegistroCont()
      contacto = contacto.EliminarCont(id)
      flash("El contacto fue eliminado!..","warning")
      return redirect(url_for('index'))

app.run(debug=True, port=5000)
