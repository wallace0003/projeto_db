class Editora:
    def __init__(self, codigo_editora: int, cnpj: str, endereco: str,
                 telefone: str, nome: str, email: str, codigo_livro: str):
        
        self.codigo_editora = codigo_editora
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.nome = nome
        self.email = email
        self.codigo_livro = codigo_livro
