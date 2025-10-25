
class Emprestimo:
    def __init__(self, codigo_emprestimo: int, codigo_pessoa: int, codigo_livro: int,
                 data_emprestimo: str, data_devolucao: str, status: str):
        
        self.codigo_emprestimo = codigo_emprestimo
        self.codigo_pessoa = codigo_pessoa
        self.codigo_livro = codigo_livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.status = status
