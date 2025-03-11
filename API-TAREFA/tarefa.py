class Tarefa:

    def __init__(self, task_id, titulo, descricao, status, duracao, prioridade, data_criacao):
        self.task_id = task_id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.duracao = duracao
        self.prioridade = prioridade
        self.data_criacao = data_criacao


    def to_json(self):
        return{
            "task_id": self.task_id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "duracao": self.duracao,
            "prioridade": self.prioridade,
            "data_criacao": self.data_criacao
        }