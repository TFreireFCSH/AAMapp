from flask import flash
from app import Error


##############################################################################
def get_options(mysql, table):
    """Creates <select> options for forms

    Function queries both `fundos` and `orgaos` relations and gathers the name
    and abbreviation for each tuple, which it then uses to compose a list of
    options that will be inserted into the <select> element of all forms that
    regard `chancelas` and other documents (e.g. `partituras`, `livros`, etc.)

                                :::PARAMETERS:::

    mysql -- A MySQLdb connection object used to query the database.
    table -- The relation to be queried.

            The only two relations accepted by this function are:
                            -->  `aam`.`fundos`
                            -->  `aam`.`orgaos`

            If another relation gets inserted an Error will be raised by the
            function.

    The output from querying the relation `fundos` should resemble the
    following:

            [
                ("", "..."),
                ("AAM", "AAM : Academia de Amadores de Música"),
                ("RAM", "RAM : Real Academia de Amadores de Música"),
                ("OGV", "OGV : Olga Violante"),
                etc.
            ]

    Here we have a list of tuples where each tuple has an option value in its
    first position, and a text description in its second. The first tuple of
    the sequence works as a placeholder.
    """
    if table == "fundos" or table == "orgaos":

        try:
            with mysql.connection.cursor() as cursor:
                query = """
                SELECT `Sigla`, `Nome` FROM `%s`;
                """ % (table,)
                get_data = cursor.execute(query)

                if get_data > 0:
                    data = cursor.fetchall()
                    sigla = [i[0] for i in data]
                    nome = [i[1] for i in data]

                    options = [("", "...")]
                    for s, n in zip(sigla, nome):
                        options.append((s, f"{s} : {n}"))

                    return options
                else:
                    return None

        except Error as err:
            print(f"There has been a problem with MySQL: {err}")

    else:
        print(f"Invalid table '{table}'. Please choose fundos or orgaos")
        # return flash(f"""Invalid table '{table}'.
        #              Please choose `fundos` or `orgaos`""")


##############################################################################
def sigla_id(mysql, table, attribute, value):
    """Gets the primary key of a tuple from another attribute

    Function queries any table to fetch the primary key of a tuple having
    another attribute present in the relation as refference.

                                :::PARAMETERS:::

    mysql -- A MySQLdb connection object used to query the database.
    table -- The relation to be queried.
    attribute -- The attribute serving as refference to get the primary key.
    value -- The value of the attribute.

    The function should return an intenger, corresponding to the solicited
    primary key, as output.
    """
    with mysql.connection.cursor() as cursor:
        query = """
            SELECT `%s_id` FROM `%s`
            WHERE `%s`='%s';
        """ % (table, table, attribute, value)

        get_data = cursor.execute(query)
        if get_data > 0:
            table_id = cursor.fetchone()
    return table_id[0]


##############################################################################
def max_id(mysql, table, table_id):
    """Gets the largest primary key number from a relation and add one to it

    Function fetches the largest primary key value from any relation in the
    database and adds one to it. To be used when inserting data into the data
    base, inplace of the auto increment attribute.

                                :::PARAMETERS:::

    mysql -- A MySQLdb connection object used to query the database.
    table -- The relation to be queried.
    table_id -- The name of the primary key.

    The function should return one plus the largest intenger serving as primary
    key to any relation present in the data base.
    """
    with mysql.connection.cursor() as cursor:
        query = """
            SELECT MAX(`%s`) + 1 FROM `%s`;
        """ % (table_id, table)

        get_data = cursor.execute(query)
        if get_data > 0:
            max_id = cursor.fetchone()
    return max_id[0]


##############################################################################
def max_num(mysql, table, fundo, doc_type, doc_num):
    """Gets the largest counting for a document type in relation to its fonds

    Function is used in relations that concern types of documents (such as
    `livros`, `partituras`, etc.) and provides the largest number of any
    subcategory of documents in relation to the fonds to which the document is
    associated with.

                                :::PARAMETERS:::

    mysql -- A MySQLdb connection object used to query the database.
    table -- The relation to be queried.
    fundo -- The three letter abbreviation of the name of the fonds.
    doc_type -- The name of the attribute that descriminates de subcategories
                of documents (`Suporte` or `Tipologia`, in `partituras` and
                every other document type respectively).
    doc_num -- The three digit identifier for the subcategory of document.


    The function should return one plus the largest intenger serving as the
    current counting for any subcategory of document in relation to its fonds.
    """
    with mysql.connection.cursor() as cursor:
        query = """
            SELECT if(MAX(`Número`) IS NULL, 1, MAX(`Número`) + 1)
            FROM `%s`
            WHERE `Fundo`='%s'
            AND `%s`='%s';
        """ % (table, fundo, doc_type, doc_num)

        get_data = cursor.execute(query)
        if get_data > 0:
            max_num = cursor.fetchone()
    return int(max_num[0])


##############################################################################
def columns_to_string(mysql, table):
    """
    Função recolhe lista com nome de atributos da tabela indicada e cria uma
    cadeia de caracteres devidamente formatada para ser concatenada com o
    query.
    """
    with mysql.connection.cursor() as cursor:
        query = """
            SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME='%s';
        """ % (table,)

        get_data = cursor.execute(query)
        if get_data > 0:
            data = cursor.fetchall()
        column_names = []
        for n in data:
            # A sintax de SQL obriga a que, em caso de existirem
            # espaços no nome dos atributos, sejam utilizados ` `
            # como demarcadores, exp: `atributo com espaços`.
            if " " in n[0]:
                column_names.append("`" + n[0] + "`")
            else:
                column_names.append(n[0])
        column_names_str = "(" + ", ".join(column_names) + ")"
    return column_names_str


##############################################################################
def data_to_dict(data, table):
    """Creates dictionary with CSS id as key and query data as values

    Function creates a dictionary where the keys consist of the CSS ids of the
    elements of the forms and the values are gathered from the data base.
    The purpose is to inject the values registed into the form so that they
    can be updated.

    """
    abrv_dict = {
        "fundos": "fd",
        "orgaos": "og",
        "chancelas": "ch",
        "partituras": "pt",
        "periodicos": "pr",
        "livros": "lv"
    }
    data_dict = {}
    num = 1
    for i in data:
        num_id = abrv_dict[table] + str(num).zfill(2)
        data_dict[num_id] = i
        num += 1
    return data_dict


##############################################################################
def select_data(mysql, table, num="all", attribute=None, value=None):
    """
    Função para a declaração SELECT de SQL, com a possibilidade de recolher um
    ou vários registos.
    """
    with mysql.connection.cursor() as cursor:

        if attribute is None and value is None:
            query = """
                SELECT * FROM `%s`;
            """ % (table,)
            get_data = cursor.execute(query)

            if get_data > 0 and num == "all":
                data = cursor.fetchall()
                columns = [i[0] for i in cursor.description]
                return data, columns

        else:
            query = """
                SELECT * FROM `%s`
                WHERE `%s`='%s';
            """ % (table, attribute, value)
            get_data = cursor.execute(query)

            if get_data > 0 and num == "all":
                data = cursor.fetchall()
                columns = [i[0] for i in cursor.description]
                return data, columns

            elif get_data > 0 and num == "one":
                data = cursor.fetchone()
                columns = [i[0] for i in cursor.description]
                return data, columns


###############################################################################
def insert_data(mysql, table, form, column_names="", table_id="", num=None):
    """
                                    INSERT DATA

    Função destinada à insertção de dados na base de dados AAM.
    """
    # Na ausência de outra indicação assume-se que o nome da chave principal
    # é idêntico ao da tabela.
    if table_id == "":
        table_id == table + "_id"
    else:
        table_id = table_id
    # Com o atributo correspondente à chave principal da tabela recolhe-se o
    # valor máximo ao qual é somado '1'.
    with mysql.connection.cursor() as cursor:
        table_id_max = max_id(mysql, table, table_id)
    # É criada uma tupla com os valores recolhidos no formulário.
    form_data = tuple(form.data.values())[:-2]
    # Caso não sejam especificadas colunas o MySQL assume que o preenchimento
    # da tabela é completo e exige que os valores correspondam à cardinalidade
    # da mesma. Neste caso é passada uma cadeia de caracteres vazia para o
    # query. Caso contrário passada uma cadeia de caracteres com os nomes dos
    # atributos entre parêntesis.
    if column_names == "":
        column_names = column_names
    else:
        column_names = "(" + column_names + ")"
    # Criação de uma lista com os valores a serem inseridos. Para que os
    # campos vazios fiquem registados como NULL na BD, é necessário que
    # sejam inseridos como None (valor equivalente em Python).
    new_form_data = [table_id_max]
    for data in form_data:
        if data == "":
            new_form_data.append(None)
        else:
            new_form_data.append(data)

            #######################################################
            # CHANCELAS ###########################################
            #######################################################
    # Extrai o valor da sigla registada,
    # conforme pertença aos fundos ou órgãos
    if 'chancelas' in table:
        if new_form_data[1] is not None:
            sigla = new_form_data[2]
        else:
            sigla = new_form_data[1]

        # Determina o caracter a constar na quarta posição da referência
        # mediante a chancela tenha ou não nomeração ou cota.
        if new_form_data[-2] == "Sim":
            numeracao = "n"
        else:
            numeracao = "c"
        # Com o valor dos atributos sigla e `Numeração / Cota` é estabelecido
        # o número da referência da chancela.
        with mysql.connection.cursor() as cursor:
            query = """
                SELECT if(MAX(`número`) IS NULL, 1, MAX(`número`) + 1)
                FROM `chancelas`
                WHERE IFNULL(`fundos_sigla`,`orgaos_sigla`)='%s'
                AND `Numeração / Cota`='%s';
            """ % (sigla, new_form_data[-2])

            get_data = cursor.execute(query)
            if get_data > 0:
                get_num = cursor.fetchone()
        # Criação de uma referência para as chancelas. Este valor é ÚNICO e
        # OBRIGATÓRIO.
        referencia = f"{sigla}{numeracao}{get_num[0]}"
        # Caso a Chancela registada corresponda a um número ou cota
        # é criada automáticamente uma nova coluna na tabela numeros_cotas
        if ('chancelas' in table) and (form.NumCota.data == "Sim"):
            with mysql.connection.cursor() as cursor:
                query = """
                    ALTER TABLE numeros_cotas
                    ADD COLUMN %s VARCHAR(10);
                """ % (referencia,)

                cursor.execute(query)
                mysql.connection.commit()

        # O número estabelecido é inserido no quarto indexante
        # da lista new_form_data.
        new_form_data.insert(1, referencia)
        new_form_data.insert(4, get_num[0])

    place_holder = ", ".join(["%s" for i in range(len(new_form_data))])
    query_insert = """
            INSERT INTO `%s`%s
            VALUES(%s);
    """ % (table, column_names, place_holder)

    with mysql.connection.cursor() as cursor:
        cursor.execute(query_insert, tuple(new_form_data))
        mysql.connection.commit()

    return flash("Registo realizado com sucesso!")


###############################################################################
def update_data(mysql, table, form, select_data,
                columns_data, attribute, value):
    """
    Função para a actualização de dados. Recebe como argumentos uma
    instância da ligação à BD, o nome da tabela, os dados do formulário
    após o preenchimento, os dados constantes em BD para o respectivo
    registo, nomes de colunas e nome valor do indexante. Constroi um query
    com os valores a serem modificados e submete-os à BD.
    """
    # Conversão dos dados do formulário numa tupla
    form_data = tuple(form.data.values())[:-2]
    select_data = select_data[1:]
    # Criação de lista com o nome das colunas formatados para que possam
    # ser inseridos na requisição.
    column_name = ["`" + i + "`" for i in columns_data[1:]]

    update_columns = []
    update_values = []
    for i, (x, y) in enumerate(zip(form_data, select_data)):
        if (y is not None) and (x == "0000-00-00"):
            pass
        elif x == "":
            update_columns.append(f"{column_name[i]}=%s")
            update_values.append(None)
        elif x != y:
            update_columns.append(f"{column_name[i]}=%s")
            update_values.append(str(x))

    columns_str = ", ".join(update_columns)
    query_update = """
                UPDATE aam.`%s`
                SET %s
                WHERE `%s`='%s';
        """ % (table, columns_str, attribute, value)

    with mysql.connection.cursor() as cursor:
        cursor.execute(query_update, tuple(update_values))
        mysql.connection.commit()

    return flash("Submetido com sucesso!")

##############################################################################


def delete_data(mysql, table, attribute, value):

    query_delete = """
            DELETE FROM `%s`
            WHERE `%s`='%s';
    """ % (table, attribute, value)

    with mysql.connection.cursor() as cursor:
        cursor.execute(query_delete)
        mysql.connection.commit()

    return flash("Registo eliminado com sucesso!")
