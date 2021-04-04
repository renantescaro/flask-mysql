import json
from dao.conexao import Conexao
from entities.pessoa import Pessoa

class PessoaDao(Conexao):
    def __init__(self):
        self.tabela   = 'pessoa'
        self.entidade = Pessoa
        super().__init__(
            self.tabela,
            self.entidade)


    def selecionar_nomes(self):
        return self.setar(
            linhas = self.selecionar(campos='id, nome') )


    def selecionar_por_id(self, id):
        return self.setar(
            linhas = self.selecionar(where='id='+str(id)) )