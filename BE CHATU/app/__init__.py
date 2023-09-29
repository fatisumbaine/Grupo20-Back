from flask import Flask, render_template , request
from config import Config
from ..database import DatabaseConnection
import csv

def init_app():
    app = Flask(__name__,static_folder=Config.STATIC_FOLDER,template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    
    #validadcion de inicio de sesion
    @app.route('/')
    def bienvenida():
        return 'Pagina de bienvenida para formulario ir a /login'
        


    def obtener_usuarios():
        
        usuarios = {}
        with open('usuarios.csv', 'r',encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                usuarios[row[0]] = row[1]
        return usuarios

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            return logearse()
        else:
            return mostrar_formulario()

    def mostrar_formulario():
        return render_template('login.html')

    def logearse():
        usuarios = obtener_usuarios()
        email = request.form['email']
        password = request.form['password']
        if usuarios.get(email) == password:
            return "Inicio de sesión exitoso"
        else:
            return "Error: Nombre de usuario o contraseña incorrectos"

    
    #buscar perfil por edad
    @app.route('/users')
    def get_users():
        register_date = request.args.get('register_date')
        if register_date is not None:
            return get_recent_users(filter = register_date)
        else:
            return get_all_users()
        

    def obtener_usuarios():
        usuarios = {}
        with open('usuarios.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                usuarios[row[0]] = row[1]
        return usuarios

    #registro de nuevo usuario
    @app.route('/registro')
    def register_user():
        body_params = request.json
        register(username = body_params.get('username'),
            firstname = body_params.get('firstname'),
            lastname = body_params.get('lastname'),
            password = body_params.get('password'))
    return "Usuario registrado"

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(auth_bp, url_prefix = '/auth')


    return app