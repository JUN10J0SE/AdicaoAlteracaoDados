#importacao  a dataclass
from dataclasses import dataclass

#criar a classe pessoa
@dataclass #todos os atrubutos sao declarados privados e tras tudo do get e set sem preciar fazer a mao
class Pessoa:
    codigo: int
    nome: str
    cpf: str
    email: str
    profissao: str

    #metodo destrutor
    def __del__(self):
        return f"objeto {self.nome} de codigo {self.codigo} destrutor."
    