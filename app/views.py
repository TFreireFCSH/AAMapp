"""
                                app.views
                                ~~~~~~~~~

    Module contains all the routs to all pages that do not contain forms.
    That includes the home page, the intro page and all pages where data
    can be consulted.

    :copyright: 2020 TFreire
    :licence: [...]
"""


from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import flash
import json

from . import app
from . import mysql
from .tools.queries import select_data
from .aamdatadict import aam_data_dict as aamdt


# Allows for the zip function to be used inside the jinja2 templates
app.jinja_env.filters["zip"] = zip


##############################################################################
# Home Page ##################################################################
##############################################################################
@app.route("/")
@app.route("/home")
def home():
    """
        Route for the home page of the app.
    """
    title = "Home Page"
    return render_template("home.html", title=title)


##############################################################################
# Introduction ###############################################################
##############################################################################
@app.route('/intro')
def intro():
    """
        Route for the intro section of the app. Where general information
        about the project can be found.
    """
    return render_template('introducao.html')


##############################################################################
# Páginas referentes à Biblioteca ############################################
##############################################################################
@app.route('/biblioteca/<string:doc>')
def biblioteca(doc):

    title = aamdt[doc]["title"]
    data, columns = select_data(mysql, aamdt[doc]["table_display"])

    data_ref = []
    for ref in data:
        data_ref.append([ref[0], ref[1]])
    return render_template('table.html',
                           columns=columns,
                           data=data,
                           title=title,
                           data_ref=data_ref)


##############################################################################
@app.route('/biblioteca/gzmusical/<string:doc>')
def gazeta_musical(doc):
    return render_template('table.html')


##############################################################################
@app.route("/biblioteca/fundos/<string:fnd>", methods=["GET", "POST"])
def fundo(fnd):
    return render_template("documents.html")


##############################################################################
@app.route("/biblioteca/<string:doc>/<string:ref>",
           methods=["GET", "POST"])
def biblioteca_doc(doc, ref):
    return render_template("documents.html")


##############################################################################
# Páginas referentes ao Arquivo ##############################################
##############################################################################
@app.route("/arquivo/<string:doc>", methods=["GET", "POST"])
def arquivo(doc):

    title = aamdt[doc]["title"]
    data, columns = select_data(mysql, aamdt[doc]["table_display"])

    data_ref = []
    for ref in data:
        data_ref.append([ref[0], ref[1]])
    return render_template('table.html',
                           columns=columns,
                           data=data,
                           title=title,
                           data_ref=data_ref)


@app.route("/arquivo/orgaos/<string:org>", methods=["GET", "POST"])
def orgao(org):
    return render_template("documents.html")


##############################################################################
# Páginas referentes às Chancelas ############################################
##############################################################################
@app.route('/chancelas/')
def chancelas():

    title = aamdt["chancelas"]["title"]
    data, columns = select_data(mysql,
                                aamdt["chancelas"]["table_display"])

    data_ref = []
    for ref in data:
        data_ref.append([ref[1], ref[2]])
    return render_template('table.html',
                           columns=columns,
                           data=data,
                           title=title,
                           data_ref=data_ref)


@app.route("/chancelas/<string:ref>", methods=["GET", "POST"])
def chancelas_reg(ref):

    title = aamdt["chancelas"]["title"]
    data, columns = select_data(mysql,
                                aamdt["chancelas"]["table_main"],
                                num="one",
                                attribute=aamdt["chancelas"]["attribute"],
                                value=ref)

    return render_template("table-chancelas.html",
                           columns=columns,
                           data=data,
                           title=title)
