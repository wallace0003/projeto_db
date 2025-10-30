
class Emprestimo:
    def __init__(self, data_emprestimo:str, data_prevista_devolucao:str, data_devolucao:str | None,
                funcionario_id: int, status:str, usuario_id:int, livro_id:int):
        self.data_emprestimo = data_emprestimo
        self.data_prevista_devolucao = data_prevista_devolucao
        self.data_devolucao = data_devolucao
        self.funcionario_id = funcionario_id
        self.status = status
        self.usuario_id = usuario_id
        self.livro_id = livro_id
