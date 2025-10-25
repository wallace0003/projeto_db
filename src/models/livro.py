
class Livro:
    def __init__(self, codigo_livro: int, titulo: str, ano_pubicacao: str,
                 categoria: str, codigo_biblioteca: int, codigo_departamento: int):
        
        self.codigo_livro = codigo_livro
        self.titulo = titulo
        self.ano_pubicacao = ano_pubicacao
        self.categoria = categoria
        self.codigo_biblioteca = codigo_biblioteca
        self.codigo_departamento = codigo_departamento
