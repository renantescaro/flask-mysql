from flask import Flask, render_template, request, redirect
from dao.pessoa_dao import PessoaDao

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'lista.html',
        pessoas = list(PessoaDao().selecionar_nomes()),
        titulo  = 'Lista de Pessoas')


@app.route('/selecionar/<id_pessoa>')
def selecionar_id(id_pessoa):
    return render_template(
        'modal.html',
        pessoa = PessoaDao().selecionar_por_id(id_pessoa)[0]
    )

app.run(host='0.0.0.0', port=5000, debug=True)