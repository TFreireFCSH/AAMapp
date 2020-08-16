"""
                                app.forms.forms
                                ~~~~~~~~~~~~~~~

    Ficheiro contém configuração dos diversos formulários a serem usados na
    aplicação. Configuração envolve a definição to tipo de campo para cada
    elemnto do formulário, assim como ferramentas de validação que ajudam na
    certificação de que os valores inseridos são válidos.

    :copyright: 2020 TFreire
    :licence: [...]
"""


from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextField
from wtforms import SubmitField
from wtforms import IntegerField
from wtforms import SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
from wtforms.validators import Length


# formulário para selecção de formulários ####################################
class ChooseDocForm(FlaskForm):
    """
    Formulário inicial a partir do qual é selecionado qual o formulário que se
    pretende preencher.
    """
    tipoDeDocumento = SelectField(
        "Registo : ",
        [DataRequired()],
        choices=[
            ("", "..."),
            ("fundos", "Fundos"),
            ("orgaos", "Órgãos"),
            ("chancelas", "Chancelas"),
            ("partituras", "Partituras"),
            ("livros", "Livros")
        ]
    )

    subDocs = IntegerField(
        "",
        render_kw={"value": 1}
    )

    submit = SubmitField("Selecionar")


# Formulário para registo de fundos ##########################################
class FormFundos(FlaskForm):

    Sigla = StringField(
        "Sigla",
        [DataRequired(),
         Length(
            min=3,
            max=3,
            message=(
                """O campo da Sigla só pode conter 3 CARACTERES."""
            )
        )],
        render_kw={"id": "fd01"}
    )

    Nome = StringField(
        "Nome",
        [DataRequired(),
         Length(
            max=50,
            message=(
                """O registo é demasiado extenso.
                Limite de 50 CARACTERES!"""
            )
        )],
        render_kw={"id": "fd02"}
    )

    NomeCompleto = StringField(
        "Nome Completo",
        render_kw={"id": "fd03"}
    )

    Grupo = SelectField(
        "Grupo",
        [DataRequired()],
        choices=[
            ("", "..."),
            ("Colectivo", "Colectivo"),
            ("Indivíduo", "Indivíduo")],
        render_kw={"id": "fd04"}
    )

    NascimentoFormacao = StringField(
        "Nascimento / Formação",
        [DataRequired(),
         Length(
            min=10,
            max=10,
            message=(
                """Datas devem ser inseridas com o
                seguinte formato: '0000-00-00'"""
            )
        )],
        default="0000-00-00",
        render_kw={"id": "fd05"}
    )

    FalecimentoExtincao = StringField(
        "Falecimento / Extinção",
        [DataRequired(),
         Length(
            min=10,
            max=10,
            message=(
                """Datas devem ser inseridas com o
                seguinte formato: '0000-00-00'"""
            )
        )],
        default="0000-00-00",
        render_kw={"id": "fd06"}
    )

    Periodo = StringField(
        "Período",
        [DataRequired(),
         Length(
            max=50,
            message=(
                """O registo é demasiado extenso.
                Limite de 50 CARACTERES!"""
            )
        )],
        render_kw={"id": "fd07"}
    )

    Proveniencia = StringField(
        "Proveniência",
        [DataRequired(),
         Length(
            max=100,
            message=(
                """O registo é demasiado extenso.
                Limite de 100 CARACTERES!"""
            )
        )],
        default="AAM Biblioteca",
        render_kw={"id": "fd08"}
    )

    DataDoDeposito = StringField(
        "Data do Depósito",
        [DataRequired(),
         Length(
            min=10,
            max=10,
            message=(
                """Datas devem ser inseridas com o
                seguinte formato: '0000-00-00'"""
            )
        )],
        default="0000-00-00",
        render_kw={"id": "fd09"}
    )

    Recepcao = StringField(
        "Recepção",
        [DataRequired(),
         Length(
            max=100,
            message=(
                """O registo é demasiado extenso.
               Limite de 100 CARACTERES!"""
            )
        )],
        default="[Desconhecida]",
        render_kw={"id": "fd10"}
    )

    Descricao = TextField(
        "Descrição",
        widget=TextArea(),
        render_kw={"id": "fd11"}
    )

    NotaBiografica = TextField(
        "Biografia",
        widget=TextArea(),
        render_kw={"id": "fd12"}
    )

    Fontes = TextField(
        "Fontes",
        widget=TextArea(),
        render_kw={"id": "fd13"}
    )

    Observacoes = TextField(
        "Observações",
        widget=TextArea(),
        render_kw={"id": "fd14"}
    )

    Submit = SubmitField("Submeter")


# Formulário para registo de órgãos ##########################################
class FormOrgaos(FlaskForm):

    Sigla = StringField(
        "Sigla",
        [DataRequired(),
         Length(
            min=3,
            max=3,
            message=(
                """O campo da Sigla só pode conter 3 CARACTERES."""
            )
        )],
        render_kw={"id": "og01"}
    )

    Nome = StringField(
        "Nome",
        [DataRequired(),
         Length(
            max=50,
            message=(
                """O registo é demasiado extenso.
                Limite de 50 CARACTERES!"""
            )
        )],
        render_kw={"id": "og02"}
    )

    Formacao = StringField(
        "Formação",
        [DataRequired(),
         Length(
            min=10,
            max=10,
            message=(
                """Datas devem ser inseridas com o
                seguinte formato: '0000-00-00'"""
            )
        )],
        default="0000-00-00",
        render_kw={"id": "og03"}
    )

    Extincao = StringField(
        "Extinção",
        [DataRequired(),
         Length(
            min=10,
            max=10,
            message=(
                """Datas devem ser inseridas com o
                seguinte formato: '0000-00-00'"""
            )
        )],
        default="0000-00-00",
        render_kw={"id": "og04"}
    )

    Periodo = StringField(
        "Período",
        [DataRequired(),
         Length(
            max=50,
            message=(
                """O registo é demasiado extenso.
                Limite de 50 CARACTERES!"""
            )
        )],
        render_kw={"id": "og05"}
    )

    EmFuncoes = SelectField(
        "Em Funções",
        [DataRequired()],
        choices=[
            ("Sim", "Sim"),
            ("Não", "Não")
        ],
        render_kw={"id": "og06"}
    )

    Descricao = TextField(
        "Descrição",
        widget=TextArea(),
        default=None,
        render_kw={"id": "og07"}
    )

    Fontes = TextField(
        "Fontes",
        widget=TextArea(),
        default=None,
        render_kw={"id": "og08"}
    )

    Observacoes = TextField(
        "Observações",
        widget=TextArea(),
        default=None,
        render_kw={"id": "og09"}
    )

    Submit = SubmitField('Submeter')


# Formulário para registo de chancelas #######################################
class FormChancelas(FlaskForm):

    IdFundos = SelectField(
        "Sigla Fundos",
        choices=[],
        default=None,
        render_kw={"id": "ch01"}
    )

    IdOrgaos = SelectField(
        "Sigla Órgão",
        choices=[],
        default=None,
        render_kw={"id": "ch02"}
    )

    DescricaoNormalizada = StringField(
        "Descrição Normalizada",
        [DataRequired(),
         Length(
            max=100,
            message=(
                """O Texto excede os 100 Caracteres disponíveis."""
            )
        )],
        render_kw={"id": "ch03"}
    )

    Data1 = StringField(
        "Data 1",
        [DataRequired(),
         Length(
            min=10,
            max=10,
            message=(
                """Datas devem ser inseridas com o
                seguinte formato: '0000-00-00'"""
            )
        )],
        default="0000-00-00",
        render_kw={"id": "ch04"}
    )

    Data2 = StringField(
        "Data 2",
        [DataRequired(),
         Length(
            min=10,
            max=10,
            message=(
                """Datas devem ser inseridas com o
                seguinte formato: '0000-00-00'"""
            )
        )],
        default="0000-00-00",
        render_kw={"id": "ch05"}
    )

    Periodo = StringField(
        "Período",
        [DataRequired(),
         Length(
            max=50,
            message=(
                """O texto excede o limite de 50 Caracteres."""
            )
        )],
        render_kw={"id": "ch06"}
    )

    Tipologia = SelectField(
        "Tipologia",
        [DataRequired()],
        choices=[
            ("Carimbo", "Carimbo"),
            ("Assinatura", "Assinatura"),
            ("Numeração", "Numeração"),
            ("Selo", "Selo"),
            ("Cota", "Cota"),
            ("Carimbo com numeração", "Carimbo com numeração"),
            ("Carimbo com cota", "Carimbo com cota"),
            ("Selo com numeração", "Selo com numeração"),
            ("Selo com cota", "Selo com cota"),
            ("Outra", "Outra")
        ],
        render_kw={"id": "ch07"}
    )

    Categoria = SelectField(
        "Categoria",
        [DataRequired()],
        choices=[
            ("Proprietário", "Proprietário"),
            ("Vendedor", "Vendedor"),
            ("Editor", "Editor"),
            ("Encadernador", "Encadernador")
        ],
        render_kw={"id": "ch08"}
    )

    NumCota = SelectField(
        "Numeração / Cota",
        [DataRequired()],
        choices=[
            ("Sim", "Sim"),
            ("Não", "Não")
        ],
        default="Não",
        render_kw={"id": "ch09"}
    )

    Observacoes = TextField(
        "Observações",
        widget=TextArea(),
        render_kw={"id": "ch10"}
    )

    Submit = SubmitField('Submeter')


# Formulário para o rsgisto de partituras ####################################
class FormPartituras(FlaskForm):

    FundoSig = SelectField(
        "Sigla Fundos",
        [DataRequired()],
        choices=[],
        render_kw={"id": "pt01"}
    )

    Suporte = SelectField(
        "Suporte",
        [DataRequired()],
        choices=[
            ("", "..."),
            ("001", "Partituras Impressas"),
            ("002", "Partituras Manuscritas"),
            ("003", "Documento Misto"),
            ("004", "Volume Encadernado (Obra Impressa Integral)"),
            ("005", "Volume Encadernado (Coleção de Obras Impressas)"),
            ("006", "Volume Encadernado (Obra Manuscrita Integral)"),
            ("007", "Volume Encadernado (Coleção de Obras Manuscritas)"),
            ("008", "Volume Encadernado (Documento Misto)")
        ],
        render_kw={"id": "pt02"}
    )

    Autor_1 = StringField(
        "Autor (Resp. Principal)",
        [DataRequired()],
        render_kw={"id": "pt03"}
    )

    Autor_2 = StringField(
        "Autor (Resp. Secundária)",
        render_kw={"id": "pt04"}
    )

    Atr2Fun = SelectField(
        "",
        choices=[
            ("", "..."),
            ("Arranjo", "Arranjo"),
            ("Revisão", "Revisão"),
            ("Transcrição", "Transcrição"),
            ("Orquestração", "Orquestração"),
            ("Instrumentação", "Instrumentação"),
            ("Edição", "Edição")
        ],
        render_kw={"id": "pt05"}
    )

    Autor_3 = StringField(
        "Autor (Resp. Secundária)",
        render_kw={"id": "pt06"}
    )

    Atr3Fun = SelectField(
        "",
        choices=[
            ("", "..."),
            ("Arranjo", "Arranjo"),
            ("Revisão", "Revisão"),
            ("Transcrição", "Transcrição"),
            ("Orquestração", "Orquestração"),
            ("Instrumentação", "Instrumentação"),
            ("Edição", "Edição")
        ],
        render_kw={"id": "pt07"}
    )

    CPRP = SelectField(
        "CPRP",
        [DataRequired()],
        choices=[
            ("Sim", "Sim"),
            ("Não", "Não")
        ],
        default="Não",
        render_kw={"id": "pt08"}
    )

    Titulo_1 = StringField(
        "Título Unificado",
        [DataRequired()],
        render_kw={"id": "pt09"}
    )

    Titulo_2 = StringField(
        "Título e Menção de Responsabilidade",
        render_kw={"id": "pt10"}
    )

    Edicao_1 = StringField(
        "Edição (Componente Impressa)",
        render_kw={"id": "pt11", "placeholder": "Comp. Impressa"}
    )

    Edicao_2 = StringField(
        "Edição (Componeente Manuscrita)",
        render_kw={"id": "pt12", "placeholder": "Comp. Manuscrita"}
    )

    Data_1 = StringField(
        "Data 1",
        [DataRequired(),
         Length(
            min=10,
            max=10,
            message=(
                """Datas devem ser inseridas com o
                seguinte formato: '0000-00-00'"""
            )
        )],
        default="0000-00-00",
        render_kw={"id": "pt13"}
    )

    Data_2 = StringField(
        "Data 2",
        [DataRequired(),
         Length(
            min=10,
            max=10,
            message=(
                """Datas devem ser inseridas com o
                seguinte formato: '0000-00-00'"""
            )
        )],
        default="0000-00-00",
        render_kw={"id": "pt14"}
    )

    Periodo = StringField(
        "Período",
        render_kw={"id": "pt15"}
    )

    Instrum = StringField(
        "Instrumentação",
        widget=TextArea(),
        render_kw={"id": "pt16"}
    )

    DescFisica = StringField(
        "Descrição Física",
        widget=TextArea(),
        render_kw={"id": "pt17"}
    )

    Dedicatorias = TextField(
        "Dedicatórias",
        widget=TextArea(),
        render_kw={"id": "pt18"}
    )

    Observacoes = TextField(
        "Observações",
        widget=TextArea(),
        render_kw={"id": "pt19"}
    )

    PresArquivo = SelectField(
        "Presente no Arquivo",
        [DataRequired()],
        choices=[
            ("Sim", "Sim"),
            ("Não", "Não")
        ],
        default="Sim",
        render_kw={"id": "pt20"}
    )

    Local = StringField(
        "Local",
        render_kw={"id": "pt21", "placeholder": "Local"}
    )

    Submit = SubmitField("Submeter")
