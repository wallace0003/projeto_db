
class Pessoa:
    def __init__(self, nome:str, cpf: str,
                 cep: str, estado: str, cidade: str, bairro: str, rua: str, numero: int,
                 email: str, tipo_pessoa: str, data_cadastro: str,
                 status_conta: str, cargo: str | None, data_admissao: str, salario: float | None, 
                 departamento_id: int | None, biblioteca_id: int | None, data_nascimento: str, 
                 biografia: str | None,
                 nacionalidade:str, endereco:str):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.email = email
        self.tipo_pessoa = tipo_pessoa
        self.data_cadastro = data_cadastro
        self.status_conta = status_conta
        self.cargo = cargo
        self.data_admissao = data_admissao
        self.salario = salario
        self.departamento_id = departamento_id
        self.biblioteca_id = biblioteca_id
        self.data_nascimento = data_nascimento
        self.biografia = biografia
        self.nacionalidade = nacionalidade
        self.endereco = endereco
