"""
                                app.forms.views
                                ~~~~~~~~~~~~~~~

    Ficheiro contém sistema de rotas para as páginas que contêm formulários.

    :copyright: 2020 TFreire
    :licence: [...]
"""


from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import flash
import json

from .. import app
from .. import mysql
from ..aamdatadict import aam_data_dict as aamdt
from ..tools.queries import get_options
from ..tools.queries import max_id
from ..tools.queries import max_num
from ..tools.queries import columns_to_string
from ..tools.queries import insert_data
from ..tools.queries import select_data
from ..tools.queries import data_to_dict
from ..tools.queries import update_data
from ..tools.queries import sigla_id
from ..tools.queries import delete_data
from .forms import ChooseDocForm

# Permite usar a função zip como filtro nas templates jinja2
app.jinja_env.filters["zip"] = zip

##############################################################################
# Selecção de Formulário #####################################################
##############################################################################


@app.route("/registodocs", methods=["GET", "POST"])
def forms():
    """
                                    SELECT FORM

    Função estabelece a rota para a página de selecção de formulários e em
    seguida redireciona a ligação para o respectivo formulário.
    """
    form = ChooseDocForm()

    if request.method == "POST" and form.validate_on_submit():
        doc = form.tipoDeDocumento.data
        num = form.subDocs.data
        return redirect(url_for("reg_form", regType=doc, num=num))

    return render_template("forms/form-select.html", form=form)


##############################################################################
# Preenchimento do formulário selecionado ####################################
##############################################################################
@app.route("/registodocs/<string:regType>/<int:num>", methods=["GET", "POST"])
def reg_form(regType, num):
    """
                                    INSERT DATA

    Função estabelece a ligação entre o formulário selecionado e o respectivo
    ficheiro HTML.
    """
    # Importação dos formulários
    form = aamdt[regType]["form"]()
    if regType == "chancelas":
        # Opções actualizadas para o elemento Select do formulário
        form.IdFundos.choices = get_options(mysql, "fundos")
        form.IdOrgaos.choices = get_options(mysql, "orgaos")
    elif regType == "partituras":
        form.FundoSig.choices = get_options(mysql, "fundos")

#############################################################################

#############################################################################

    # validação do formulário, submissão e redirecionamento da página
    if request.method == "POST" and form.validate_on_submit():
        insert_data(mysql,
                    aamdt[regType]["table_insert"],
                    form,
                    table_id=aamdt[regType]["table_id"])

        if regType == "chancelas":
            return redirect(url_for(aamdt[regType]["page"]))
        else:
            return redirect(url_for(aamdt[regType]["page"], doc=regType))

    html_form = f"forms/form-{regType}.html"
    return render_template(html_form, form=form)


##############################################################################
# Registo da Chancelas por documento #########################################
##############################################################################
@app.route("/registochancelas/<string:num>/<string:doc>/<string:ref>",
           methods=["GET", "POST"])
def reg_chancelas(num, doc, ref):
    """
                        ATRIBUIÇÃO DE CHANCELAS

    Página remete para formulário no qual são associadas aos diversos
    documentos as chancelas, numeradas ou não, que estes contêm.
    """
    # Recolha de referênciase path de imagens para oformulário
    if num == 'notnum':
        table_select = "view_chancelas_not_num"
        table_insert = "chancelas_periodicos"
        template = "reg-chancelas.html"
    elif num == 'num':
        table_select = "view_chancelas_num"
        table_insert = "numeracoes_cotas"
        template = "reg-chancelas-num.html"

    data, columns = select_data(mysql, table_select)

    # Referência corresponde ao nome dos campos de input checkbox para as
    # chancelas não numeradas
    referencias = []
    for i in data:
        checkbox_name = "checkbox-" + i[1]
        referencias.append(checkbox_name)

    # Resgisto de chancelas não numeradas ####################################
    if request.method == "POST" and num == "notnum":
        doc_id = "2"
        request_data = []
        for name in referencias:
            checkbox_data = request.form.get(name)
            if checkbox_data is not None:
                request_data.append(checkbox_data)

        with mysql.connection.cursor() as cursor:
            for dt in request_data:
                table_id = max_id(mysql, table_insert)
                query = """
                    INSERT INTO aam.%s
                    VALUES (%s, %s, %s);
                """ % (table_insert, table_id, doc_id, dt)
                cursor.execute(query)
                mysql.connection.commit()

        return f"<h3>{referencias}</h3> <br> <h3>{request_data}</h3>"

    # Registo de chancelas numeradas ##########################################
    # Nome das colunas para o registo
    column_names = []
    for i in data:
        column_names.append(i[1])

    if request.method == "POST" and num == "num":
        request_data = []

        for name in referencias:
            checkbox_data = request.form[name]
            request_data.append(checkbox_data)

        data_for_submition = []
        colm_for_submition = []
        for col, dt in zip(column_names, request_data):
            if dt != "":
                data_for_submition.append(str(dt))
                colm_for_submition.append(col)

        return f"""<h3>{data[0]}</h3>
                    <br><h3>{referencias}</h3>
                    <br><h3>{request_data}</h3>
                    <br><h3>{', '.join(data_for_submition)}</h3>
                    <br><h3>{', '.join(colm_for_submition)}</h3>"""

    return render_template(template, data=data, columns=columns)


##############################################################################
# Actuaização e alteração de dados ###########################################
##############################################################################
@app.route("/updateform/<string:regType>/<string:ref>",
           methods=["GET", "POST"])
def update_form(regType, ref):
    """
                                CHANGE DATA

    Rota para formulário de actualização de valores. O formulário neste caso,
    recebe os valores constantes na base de dados para um respectivo registo,
    como valores por defeito, e insere novos valores na base de dados no caso
    de serem realizadas alterações."""

    form = aamdt[regType]["form"]()

    if regType == "chancelas":
        form.IdFundos.choices = get_options(mysql, 'fundos')
        form.IdOrgaos.choices = get_options(mysql, 'orgaos')
    if regType == "partituras":
        form.FundoSig.choices = get_options(mysql, 'fundos')
    # Importação dos dados da BD que serão utilizados como valores de
    # referência no formulário
    data, columns = select_data(mysql,
                                aamdt[regType]["table_update"],
                                num="one",
                                attribute=aamdt[regType]["attribute"],
                                value=ref)
    # Dicionário contem valores extraidos da BD com o id CSS como chave.
    # Permite inserir os valores existentes como referência para a
    # actualização.
    data_dict = data_to_dict(data[1:], regType)
    table_id = data[0]
    # Após a actualização dos valores o formulário é submetido e ambas
    # as tuplas, a proveniente da função select_data e a resultante de
    # preenchimento do formulário, serão inseridas como parametros na
    # função update_data que as comparará e fará o registo apenas para
    # os valores que apresentarem alterações.
    if request.method == "POST" and form.validate_on_submit():
        update_data(mysql,
                    aamdt[regType]["table_update"],
                    form,
                    data,
                    columns,
                    aamdt[regType]["attribute"],
                    ref)

        return redirect(url_for(aamdt[regType]["page"], doc=regType))

    htmlForm = f"forms/form-{regType}.html"
    return render_template(htmlForm,
                           form=form,
                           data=json.dumps(data_dict, default=str),
                           update=True)


##############################################################################
# Eliminação de dados ########################################################
##############################################################################
@app.route("/deleterecord/<string:regType>/<string:ref>",
           methods=["GET", "POST"])
def delete_form(regType, ref):
    """
                                DELETE DATA

    Página de confirmação para a eliminação de registos. Apresenta uma
    tabela com todos os atributos e valores do registo a ser eliminado e pede
    confirmação.Caso se confirme, o registo é eliminado da base de dados e a
    página é redirecionada para a página com a tabela à qual o registo
    pertencia.

    """
    # Selecção da tupla contendo os dados a serem eliminados.Para este
    # efeito a tupla provem da relação principal e não de uma vista.
    data, columns = select_data(
        mysql,
        aamdt[regType]["table_main"],
        num="one",
        attribute=aamdt[regType]["attribute"],
        value=ref
    )

    # Submissão da acção de eliminação de registo ou cancelamento.
    if request.method == "POST":
        # Se o botão "Confirmar", que contém o valor "True", for accionado a
        # função "delete_data" é aplicada.
        if request.form["button-delete"] == "True":
            delete_data(mysql,
                        table=regType,
                        attribute=aamdt[regType]["attribute"],
                        value=ref)

            return redirect(url_for(aamdt[regType]["page"],
                                    doc=regType))
        # Caso o botão "Cancelar" seja acionado, somos apenas redirecionados
        # para a página com a tabela correspondente ao registo que
        # considerámos apagar.
        else:
            return redirect(url_for(aamdt[regType]["page"],
                                    doc=regType))

    return render_template('delete-confirm.html',
                           regType=regType,
                           ref=ref,
                           data=data,
                           columns=columns)
