
class Livro:
    def __init__(self, titulo: str, ano_pubicacao: str,
                editora_id: int, biblioteca_id: int, autor:str, isbn:str):
        self.titulo = titulo
        self.ano_pubicacao = ano_pubicacao
        self.editora_id = editora_id
        self.biblioteca_id = biblioteca_id
        self.autor = autor
        self.isbn = isbn
