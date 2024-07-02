from config import *

class Tarefa(db.Entity):
    nomeDaTarefa = Required(str)
    objetivoDaTarefa = Required(str)
    concluidaOuNaoConcluida = Optional(str)
    dataDaTarefa = Optional(str)
    pessoaResponsavel = Optional(str)
    def __str__(self):
        return f'{self.nomeDaTarefa}, {self.objetivoDaTarefa}, {self.concluidaOuNaoConcluida}, {self.dataDaTarefa}, {self.pessoaResponsavel}'
db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)