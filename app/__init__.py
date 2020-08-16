"""
                                    AAMapp
                                    ~~~~~~

    Página web e aplicação para introdução, consulta e modificação de dados
    referntes ao arquivo e biblioteca da Academia de Amadores de Música de
    Lisboa.

    :copyright: 2020 TFreire
    :licence: [...]
"""

from flask import Flask
from flask_mysqldb import MySQL
from MySQLdb.connections import Error

# Cria uma instância da classe Flask, o que corresponde a uma aplicação.
app = Flask(__name__, )
# Estabelece a ligação entre a aplicação e o sistema de gestão de base de
# dados MySQL.
mysql = MySQL(app)


# Invoca diferentes subclasses de configuração em função do ambiente definido.
if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV'] == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

# Importa o sistema de rotas entre as diferentes páginas.
from . import views
from .forms import views
