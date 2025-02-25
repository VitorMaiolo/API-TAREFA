from flask import Flask, request


app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "Estudar Javcascript",
        "descricao": "Estudar JS para aprender eventos",
        "status": "Em andamento",
        "duracao": "2 horas",
        "prioridade": "Alta",
        "data_criacao": "25.02.2025"

    },
    {
        "id": 2,
        "titulo": "Estudar Flask",
        "descricao": "Estudar Flask para aprender sobre web services",
        "status": "Não iniciado",
        "duracao": "1 hora",
        "prioridade": "Alta",
        "data_criacao": "25.02.2025"
    }
]

#Retorna as tarefas
@app.route('/tasks', methods=['GET'])
def get_task():
    return tarefas

#Retorna pelo ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return tarefa
        else:
            return "Tarefa Não Encontrada"



@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    return "Tarefa Criada Com Sucesso"
    return task


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None

    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['duracao'] = task_body.get('duracao')
    task_search['prioridade'] = task_body.get('prioridade')
    task_search['data_criacao'] = task_body.get('data_criacao')



    return task_search


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa['id'] == task_id:
            tarefas.remove(tarefa)
            return "Tarefa removida"




if __name__ == '__main__':
    app.run(debug=True)


