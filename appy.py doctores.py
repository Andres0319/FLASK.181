from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbConsultorio'
app.secret_key='mysecretkey'
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('interfaz grafica.html')

@app.route('/inicio')
def inicio():
    return render_template('interfaz doctores.html')

@app.route('/adminMed')
def administracionMedicos():
    return render_template('Administracion medicos.html')

@app.route('/administracionMedicos2', methods=['GET','POST'])
def administracionMedicos2():
    if request.method == 'POST':

        #pasamos a variables el contenido de los input 
        vtitulo= request.form['nombre']
        vartista= request.form['apellido']
        vanio= request.form['correo']

        cs = mysql.connection.cursor()
        cs.execute('insert into Medicos(nombre,ap,correo) values (%s,%s,%s)', (vtitulo,vartista,vanio))
        mysql.connection.commit()

    flash('El doctor fue agregado correctamente')
    return render_template('Administracion medicos 2.html')

@app.route('/administracionMedicos3')
def administracionMedicos3():
    return render_template('Administracion medicos 3.html')

@app.route('/citasConsultas')
def citasConsultas():
    return render_template('Citas consultas.html')

@app.route('/citasConsultas2')
def citasConsultas2():
    return render_template('Citas consultas 2.html')

@app.route('/citasConsultas3')
def citasConsultas3():
    return render_template('Citas consultas 3.html')

@app.route('/citasConsultas4')
def citasConsultas4():
    return render_template('Citas consultas 4.html')

@app.route('/citasConsultas5')
def citasConsultas5():
    return render_template('Citas consultas 5.html')

@app.route('/consultarPacientes')
def consultarPacientes():
    return render_template('Consultar Pacientes.html')

@app.route('/consultarPacientes2')
def consultarPacientes2():
    return render_template('Consultar Pacientes 2.html')

@app.route('/consultarPacientes3')
def consultarPacientes3():
    return render_template('Consultar Pacientes 3.html')

@app.route('/consultarPacientes4')
def consultarPacientes4():
    return render_template('Consultar Pacientes 4.html')

@app.route('/expedientePacientes', methods=['GET','POST'])
def expedientePacientes():
    if request.method == 'POST':
        VNombre=request.form['nombre']
        VApellido_paterno=request.form['apellidoPaterno']
        VApellido_materno=request.form['apellidoMaterno']
        VFecha_de_nacimiento=request.form['fechaNacimiento']
        VNacionalidad=request.form['nacionalidad']
        VSexo=request.form['sexo']
        curp=request.form['curp']
        VCorreo=request.form['correo']
        VTipo_de_sangre=request.form['tipoSangre']
        VTelefono=request.form['telefonoCelular']
        VDireccion=request.form['direccion']
        VColonia=request.form['colonia']
        cp=request.form['codigoPostal']
        VEntidad_federativa=request.form['entidadFederativa']
        VMunicipio=request.form['municipio']
        VEstado=request.form['estado']
        vmedico=request.form['medicoAtiende']
        cs= mysql.connection.cursor()
        cs.execute('insert into Pacientes(nombre,ap,apellidoM,fechaNac,nacionalidad,sexo,curp,correo,tipoSangre,telefono,direccion,colonia,cp,entidadFed,municipio,estado,idMedico) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (VNombre,VApellido_paterno,VApellido_materno,VFecha_de_nacimiento,VNacionalidad,VSexo,curp,VCorreo,VTipo_de_sangre,VTelefono,VDireccion,VColonia,cp,VEntidad_federativa,VMunicipio,VEstado,vmedico))
        mysql.connection.commit()


    flash('El doctor fue agregado correctamente')
    return render_template('Expediente Pacientes.html')

@app.route('/expedientePacientes2')
def expedientePacientes2():
    return render_template('Expediente Pacientes 2.html')

@app.route('/exploracion_diagnostico')
def exploracion_diagnostico():
    return render_template('Exploracion y diagnostico.html')

@app.route('/exploracion_diagnostico2')
def exploracion_diagnostico2():
    return render_template('Exploracion y diagnostico 2.html')

@app.route('/exploracion_diagnostico3')
def exploracion_diagnostico3():
    return render_template('Exploracion y diagnostico 3.html')

@app.route('/exploracion_diagnostico4')
def exploracion_diagnostico4():
    return render_template('Exploracion y diagnostico 4.html')

@app.route('/exploracion_diagnostico5')
def exploracion_diagnostico5():
    return render_template('Exploracion y diagnostico 5.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)