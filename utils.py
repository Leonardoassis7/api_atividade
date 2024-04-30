from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Leonardo', idade=26)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Leonardo').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Bruno").first()
    pessoa.idade = 21
    pessoa.save()

def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Bruno').first()
    pessoa.delete()

if __name__ == '__main__':
    altera_pessoa()