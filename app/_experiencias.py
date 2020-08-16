nomes = ('coluna', 'coluna2', 'coluna com espaços', 'coluna coluna', 'e mais uma', 'última')



colName = {}
for i, name in enumerate(nomes):
    if ' ' in name:
        colName[i] = "`"+ name +"`"
    else:
        colName[i] = name

print(tuple(colName.values()))


valoresSelect = ('sim', 'não', 'talvez', 'sim', 'sim', 'não sei')

valoressUpdate = ('sim', 'não', 'não', 'sim', 'não', 'já sei')

indx = 0
name_val = []
for x, y in zip(valoresSelect, valoressUpdate):
    if x != y:
        name_val.append((colName[indx], y))
    indx += 1

print(name_val)


col_query = []
for t in name_val:
    col_query.append(str(t[0]) + '=' + str('"' + t[1] + '"'))

col_query_str = ', '.join(col_query)

print(col_query_str)

id = 2

query = f"""UPDATE fundos SET {col_query_str} WHERE fundos_id={id};"""


print(query)

l1 = ['cena', 'e', 'tal', '', '']
values = ('um', None)
str_teste = """parametro 1 = %s, 2 = %s"""
print(str_teste % (values[0], values[1]))


place_holder_list = ", ".join(["%s" for i in range(12)])

print(place_holder_list)

teste_str = "INSERT INTO aam.%s%s VALUES (%s);" % ("chancelas_periodicos", "", "231, 1234 | 98")
print(teste_str)

regType = "fundos"

def function(x, y):
    return x + y

teste_dict = {
        "fundos": {
            "page": "biblioteca",
            "title": "AAM Fundos",
            "table_main": "view_fundos",
            "form": "FormFundos",
            "attribute": "Sigla",
            "function": function
        },
         "orgaos": {
            "page": "arquivo",
            "title": "AAM Órgãos",
            "table_main": "view_orgaos",
            "form": "FormOrgaos",
            "attribute": "Sigla"
        }
}
print(teste_dict[regType]["function"](1, 5))


teste_list = [1, 5, 451, 0.12]

teste_list.insert(2, 561)

print(teste_list)

num = 12
i = 1

while i <= num:
    print("do this!")
    i += 1



assert len(queries.get_options(app.mysql, "fundos")[1][0]) == 3
assert isinstance(queries.get_options(app.mysql, "fundos")[1][0], str)
assert len(queries.get_options(app.mysql, "orgaos")[1][0]) == 3
assert isinstance(queries.get_options(app.mysql, "orgaos")[1][0], str)
assert queries.get_options(app.mysql, "partituras") == None

assert ininstance(queries.get_options(app.mysql, "fundos"), list)
assert ininstance(queries.get_options(app.mysql, "fundos")[0], tuple)
assert len(queries.get_options(app.mysql, "fundos")[0]) == 2



import random

def tables():
    tables = (
        ("fundos",),
        ("orgaos",),
        ("chancelas",),
        ("periodicos",),
        ("periodicos_numeros",),
        ("partituras")
    )
    return tables

    # tuple(random.sample(tables, 1))

tables()
