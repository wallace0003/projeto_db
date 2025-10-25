
class Pessoa:
    def __init__(self, codigo_pessoa: int, nome: str, sobrenome: str, cpf: str,
                 cep: str, estado: str, cidade: str, bairro: str, rua: str, numero: int,
                 complemento: str, logradouro: str, email: str, tipo_pessoa: str, data_cadastro: str,
                 status_conta: str, cargo: str, data_admissao: str, salario: float, codigo_departamento: int,
                 cod_biblioteca: int, data_nascimento: str, biografia: str):
        
        self.codigo_pessoa = codigo_pessoa
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.cep = cep
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.logradouro = logradouro
        self.email = email
        self.tipo_pessoa = tipo_pessoa
        self.data_cadastro = data_cadastro
        self.status_conta = status_conta
        self.cargo = cargo
        self.data_admissao = data_admissao
        self.salario = salario
        self.codigo_departamento = codigo_departamento
        self.cod_biblioteca = cod_biblioteca
        self.data_nascimento = data_nascimento
        self.biografia = biografia
