"""
                            app.aamdatadict
                            ~~~~~~~~~~~~~~~

    Ficheiro contém dicionário que agrega informação de base sobre os
    diferentes componentes dos dados, organizado por tipo de dados. O
    objectivo é facilitar a comunicação de valores às diversas rotas.

    :copyright: 2020 TFreire
    :licence: [...]
"""


from .forms.forms import FormFundos
from .forms.forms import FormOrgaos
from .forms.forms import FormChancelas
from .forms.forms import FormPartituras


aam_data_dict = {
        "fundos": {
            "page": "biblioteca",
            "title": "AAM Fundos",
            "table_id": "fundos_id",
            "table_main": "fundos",
            "table_display": "view_fundos",
            "table_insert": "fundos",
            "table_update": "fundos",
            "form": FormFundos,
            "attribute": "Sigla"
        },
        "orgaos": {
            "page": "arquivo",
            "title": "AAM Órgãos",
            "table_id": "orgaos_id",
            "table_main": "orgaos",
            "table_display": "view_orgaos",
            "table_insert": "orgaos",
            "table_update": "orgaos",
            "form": FormOrgaos,
            "attribute": "Sigla"
        },
        "chancelas": {
            "page": "chancelas",
            "title": "AAM Chancelas",
            "table_id": "chancelas_id",
            "table_main": "chancelas",
            "table_display": "view_chancelas",
            "table_insert": "view_chancelas_insert",
            "table_update": "view_chancelas_update",
            "form": FormChancelas,
            "attribute": "Referência"
        },
        "catgeraldocumentos": {
            "page": "arquivo",
            "title": "AAM Órgãos | Catálogo Geral de Documentos",
            "table_main": "orgaos",
            "table_display": "view_orgaos",
            "form": None,
            "attribute": "Sigla"
        },
        "periodicos": {
            "page": "biblioteca",
            "title": "Periódicos",
            "table_main": "periodicos_numeros",
            "table_display": "view_periodicos_numeros",
            "form": None,
            "attribute": "Referência"
        },
        "partituras": {
            "page": "biblioteca",
            "title": "Partituras",
            "table_main": "partituras",
            "table_display": "view_partituras",
            "table_insert": "view_partituras_insert",
            "table_update": "view_partituras_update",
            "form": FormPartituras,
            "attribute": "Referência"
        },
        "livros": {
            "page": "biblioteca",
            "title": "Livros",
            "table_main": "view_livros",
            "form": None,
            "attribute": "Referência"
        },
        "gravuras": {
            "page": "biblioteca",
            "title": "Gravuras Geral",
            "table_main": "view_gravuras",
            "form": None,
            "attribute": "Referência"
        }
}
