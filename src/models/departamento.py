class Departamento:
    def __init__(self, codigo_departamento: int, nome: str, descricao: str, responsavel: str,
                 codigo_funcionario: int, codigo_pessoa: int):
        
        self.codigo_departamento = codigo_departamento
        self.nome = nome
        self.descricao = descricao
        self.responsavel = responsavel
        self.codigo_funcionario = codigo_funcionario
        self.codigo_pessoa = codigo_pessoa
