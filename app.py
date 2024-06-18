from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost:3306/casalista'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Profesion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profesion = db.Column(db.String(100))

    #Relaciones
    profesion_usuario = db.relationship('Usuarios', backref='profesion', lazy=True)

    def __init__(self, profesion):
        self.profesion = profesion

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(128), nullable=False)
    zona = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(4), nullable=False)
    imagen = db.Column(db.String(1000), nullable=False)
    profesion_id = db.Column(db.Integer, db.ForeignKey('profesion.id'))
    valoracion_media_profesional = db.Column(db.Numeric(precision=3, scale=2))
    descripcion_profesional = db.Column(db.String(1000))

    #Relaciones
    pedidos_realizados = db.relationship('Pedidos', foreign_keys='Pedidos.cliente_id', backref='cliente', lazy=True)
    pedidos_recibidos = db.relationship('Pedidos', foreign_keys='Pedidos.profesional_id', backref='profesional', lazy=True)

    pedido_evaluado_cliente = db.relationship('Valoracion', foreign_keys='Valoracion.cliente_id', backref='cliente', lazy=True)
    pedido_evaluado_profesional = db.relationship('Valoracion', foreign_keys='Valoracion.profesional_id', backref='profesional', lazy=True)

    def __init__(self, nombre, apellido, mail, contrasena, zona, telefono, genero, imagen):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.contrasena = contrasena
        self.zona = zona
        self.telefono = telefono
        self.genero = genero
        self.imagen = imagen

class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    profesional_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    fecha_realizado = db.Column(db.DateTime)

    def __init__(self, cliente_id, profesional_id):
        self.cliente_id = cliente_id
        self.profesional_id = profesional_id

class Valoracion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    profesional_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    valoracion_media_individual = db.Column(db.Numeric(precision=3, scale=2))
    comentario = db.Column(db.String(400), nullable=False)

    def __init__(self, cliente_id, profesional_id, valoracion_media_individual, comentario):
        self.cliente_id = cliente_id
        self.profesional_id = profesional_id
        self.valoracion_media_individual = valoracion_media_individual
        self.comentario = comentario

with app.app_context():
    db.create_all()

    '''
    #Agregar profesiones la primera vez
    profesiones = ["Electicista", "Gasista", "Plomero", "Carpintero", "Jardinero", "Cerrajero", "Aire acondicionado", "Pintor", "Albañil", "Fletero"]

    for agregar_profesion in profesiones:
        nueva_profesion = Profesion(profesion=agregar_profesion)
        db.session.add(nueva_profesion)
        db.session.commit()
    '''
    '''
    data_serializada = []
    
    for profesion in Profesion.query.all():
        data_serializada.append({"id":profesion.id, "profesion":profesion.profesion})

    print(data_serializada)
    '''

@app.route("/") 
def index():
    return f'App Web de CasaLista'


@app.route("/altaUsuario", methods=['POST'])
def alta_usuario():
    
    nombre = request.json["nombre"]
    apellido = request.json["apellido"]
    mail = request.json["mail"]
    zona = request.json["zona"]
    telefono = request.json["telefono"]
    genero = request.json["genero"]
    imagen = request.json["imagen"]
    contrasena = request.json["contrasena"]

    nuevo_usuario = Usuarios(nombre=nombre, apellido=apellido, mail=mail, zona=zona, telefono=telefono, genero=genero, imagen=imagen, contrasena=contrasena)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        'id': nuevo_usuario.id
    }), 201

@app.route("/consultaUsuario/<id>", methods=['GET'])
def consulta_usuario(id):
    usuario_consulta = Usuarios.query.get(id)

    usuario_profesion = None

    if usuario_consulta.profesion_id is not None:
        usuario_profesion = usuario_consulta.profesion.profesion
    
    return jsonify({
        'id': usuario_consulta.id,
        'nombre': usuario_consulta.nombre,
        'apellido': usuario_consulta.apellido,
        'mail': usuario_consulta.mail,
        'zona': usuario_consulta.zona,
        'telefono': usuario_consulta.telefono,
        'genero': usuario_consulta.genero,
        'imagen': usuario_consulta.imagen,
        'contrasena': usuario_consulta.contrasena,
        'profesion': usuario_profesion,
        'descripcion_profesion': usuario_consulta.descripcion_profesional
    }), 200

@app.route("/correoExistente", methods=['GET'])
def usuario_existente():
    mail = request.args.get("mail")
    usuario_consulta = Usuarios.query.filter_by(mail=mail).first()

    if usuario_consulta is None:
        return jsonify({'existe': False}), 200
    else:
        return jsonify({'existe': True}), 200


@app.route("/loginUsuario", methods=['POST'])
def login_usuario():
    data = request.get_json()

    mail = data["mail"]
    contrasena = data["contrasena"]

    usuario = Usuarios.query.filter_by(mail=mail).first()

    if not usuario or usuario.contrasena != contrasena:
        return jsonify({'mensaje': 'usuario y/o contraseña no válidos'}), 401
    
    return jsonify({
            'mensaje': 'inicio exitoso',
            'id': usuario.id
    }), 200


@app.route('/actualizarPerfil/<id>', methods=['PUT'])
def update(id):
    usuario = Usuarios.query.get(id)

    mail = request.json["mail"]
    nombre = request.json["nombre"]   
    apellido = request.json["apellido"]
    zona = request.json["zona"]
    genero = request.json["genero"]
    telefono = request.json["telefono"]
    imagen = request.json["imagen"]
    contrasena = request.json["contrasena"]
    
    profesion_nombre = request.json["profesion"]

    descripcion_profesional = request.json["descripcion"]

    if profesion_nombre is not None:
        profesion = Profesion.query.filter_by(profesion=profesion_nombre).first()
        usuario.profesion_id = profesion.id
        usuario.descripcion_profesional = descripcion_profesional
    else:
        usuario.profesion_id = None
        usuario.descripcion_profesional = None
    
    usuario.mail = mail
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.zona = zona
    usuario.genero = genero
    usuario.telefono = telefono
    usuario.imagen = imagen
    usuario.contrasena = contrasena

    db.session.commit()

    return jsonify({
            'mensaje': 'Datos actualizados correctamente'
    }), 200


@app.route('/solicitarEspecialistas', methods=['GET'])
def listado_especialistas():
    especialistas = Usuarios.query.filter(Usuarios.profesion_id.isnot(None)).all()

    listado_especialistas = []
    
    for especialista in especialistas:
        profesion = Profesion.query.filter_by(id=especialista.profesion_id).first()
        listado_especialistas.append({
            'id': especialista.id,
            'nombre': especialista.nombre,
            'apellido': especialista.apellido,
            'telefono': especialista.telefono,
            'zona': especialista.zona,
            'foto_perfil': especialista.imagen,
            'profesion': profesion,
            'descripcion': especialista.descripcion_profesional
        })

    return jsonify(listado_especialistas), 200

if __name__ == "__main__":
    app.run(debug=True)