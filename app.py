from config import *
from model import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar_tarefas")
def listar_tarefas():
    with db_session:
        # obtém as tarefas
        tarefas = Tarefa.select() 
        return render_template("listar_tarefas.html", tarefas=tarefas)

@app.route("/form_adicionar_tarefas")
def form_adicionar_tarefas():
    return render_template("form_adicionar_tarefas.html")

@app.route("/adicionar_tarefas")
def adicionar_tarefas():
    # obter os parâmetros
    nomeDaTarefa = request.args.get("nomeDaTarefa")
    objetivoDaTarefa = request.args.get("objetivoDaTarefa")
    concluidaOuNaoConcluida = request.args.get("concluidaOuNaoConcluida")
    dataDaTarefa = request.args.get("dataDaTarefa")
    pessoaResponsavel = request.args.get("pessoaResponsavel")
    # salvar
    with db_session:
        # criar a tarefa
        t = Tarefa(**request.args)
        # salvar
        commit()
        # encaminhar de volta para a listagem
        return redirect("listar_tarefas") 

'''
run:
$ flask run
'''