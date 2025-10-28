from faker import Faker
from datetime import datetime
from random import randint, choice
from src.models.pessoa import Pessoa
from src.models.biblioteca import Biblioteca
from src.models.editora import Editora
from src.models.livro import Livro

#Instanciando a classe faker
fake = Faker("pt-br")
start_date = datetime(2000, 1, 1)
end_date = datetime(2025,12,31)

ceps = [
    "01001-000", "01310-200", "02012-030", "04045-002", "05010-040",
    "20040-020", "20271-110", "20511-000", "21010-080", "22041-001",
    "30110-012", "30260-120", "30575-180", "30710-290", "31015-060",
    "40026-010", "40255-000", "40353-040", "40420-160", "40725-340",
    "80010-000", "80210-150", "80320-080", "80530-100", "80740-390"
]

bairros = [
    "Centro", "Jardim Paulista", "Bela Vista", "Pinheiros", "Moema",
    "Copacabana", "Ipanema", "Botafogo", "Tijuca", "Leblon",
    "Savassi", "Lourdes", "Pampulha", "Santa Efigênia", "Funcionários",
    "Pelourinho", "Barra", "Itaigara", "Rio Vermelho", "Pituba",
    "Batel", "Bigorrilho", "Água Verde", "Centro Cívico", "Santa Felicidade"
]

ruas = [
    "Rua XV de Novembro", "Avenida Paulista", "Rua da Consolação", "Rua Augusta", "Rua Oscar Freire",
    "Avenida Atlântica", "Rua Barata Ribeiro", "Rua Voluntários da Pátria", "Rua São Clemente", "Rua Marquês de Abrantes",
    "Avenida Afonso Pena", "Rua da Bahia", "Rua dos Timbiras", "Rua São Paulo", "Avenida do Contorno",
    "Rua Chile", "Avenida Sete de Setembro", "Rua Carlos Gomes", "Rua Direita", "Rua da Graça",
    "Rua Marechal Deodoro", "Avenida Silva Jardim", "Rua XV de Novembro", "Rua Padre Anchieta", "Rua Itupava"
]

complementos = [
    "Apto 101 - Bloco A", "Casa 2", "Fundos", "Cobertura", "Sala 305",
    "Apto 402 - Torre B", "Casa de Esquina", "Loja 01", "Sobreloja", "Apto 12",
    "Bloco C - Apto 56", "Galpão 3", "Anexo", "Apto 901", "Loja 5",
    "Casa dos fundos", "Apto térreo", "Cobertura duplex", "Bloco D", "Apto 203",
    "Kitnet 08", "Sobrado", "Térreo", "Apto 405", "Casa principal"
]


estados_cidades = {
    "SP": ["São Paulo", "Campinas", "Santos", "Sorocaba", "Ribeirão Preto"],
    "RJ": ["Rio de Janeiro", "Niterói", "Petrópolis", "Volta Redonda", "Campos dos Goytacazes"],
    "MG": ["Belo Horizonte", "Uberlândia", "Juiz de Fora", "Contagem", "Montes Claros"],
    "RS": ["Porto Alegre", "Caxias do Sul", "Pelotas", "Santa Maria", "Passo Fundo"],
    "PR": ["Curitiba", "Londrina", "Maringá", "Cascavel", "Ponta Grossa"],
    "SC": ["Florianópolis", "Joinville", "Blumenau", "Chapecó", "Itajaí"],
    "BA": ["Salvador", "Feira de Santana", "Vitória da Conquista", "Ilhéus", "Itabuna"],
    "PE": ["Recife", "Olinda", "Caruaru", "Petrolina", "Garanhuns"],
    "CE": ["Fortaleza", "Juazeiro do Norte", "Sobral", "Crato", "Maracanaú"],
    "GO": ["Goiânia", "Anápolis", "Rio Verde", "Luziânia", "Aparecida de Goiânia"],
    "PA": ["Belém", "Santarém", "Marabá", "Ananindeua", "Castanhal"],
    "AM": ["Manaus", "Parintins", "Itacoatiara", "Manacapuru", "Coari"],
    "MT": ["Cuiabá", "Várzea Grande", "Rondonópolis", "Sinop", "Tangará da Serra"],
    "MS": ["Campo Grande", "Dourados", "Três Lagoas", "Corumbá", "Ponta Porã"],
    "DF": ["Brasília"]
}

tipos_pessoas = ["USUARIO", "FUNCIONARIO", "AUTOR"]
status_conta = ["ATIVO", "INATIVO", "SUSPENSO"]
cargos_biblioteca = ["Bibliotecário","Assistente de Biblioteca", "Auxiliar de Biblioteca",
                     "Atendente de Biblioteca", "Gerente de Biblioteca"]

biografias = [
    "Autor apaixonado por literatura clássica e contos contemporâneos.",
    "Escritora dedicada à divulgação científica e educação ambiental.",
    "Poeta urbano que transforma o cotidiano em versos inspiradores.",
    "Romancista que explora temas de amor, perda e autodescoberta.",
    "Jornalista e cronista com foco em histórias da vida real.",
    "Pesquisadora da cultura popular e das tradições regionais.",
    "Autor de ficção científica interessado em futuros alternativos.",
    "Escritor independente que mistura humor e crítica social.",
    "Professora e contista com obras voltadas ao público juvenil.",
    "Historiador e biógrafo que retrata grandes nomes da literatura."
]

def make_people(n_peoples: int) -> list:
    pessoas = []
    for i in range(1, n_peoples + 1):
        estado = choice(list(estados_cidades.keys()))
        cidade = choice(estados_cidades[estado])
        bairro = choice(bairros)
        rua = choice(ruas)
        cep = choice(ceps)
        numero = randint(1, 1000)
        nome = fake.name()
        cpf = fake.cpf()
        email = fake.email()
        tipo = choice(tipos_pessoas)
        data_cadastro = fake.date_between(start_date, end_date)
        data_admissao = fake.date_between(start_date, end_date)
        status = choice(status_conta)
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
        nacionalidade = choice(["Brasileiro", "Venezuelano", "Canadense","Americano","Argentino"])
        endereco = f"{rua}, {numero} - {bairro}, {cidade}/{estado}, CEP {cep}"

        # Campos opcionais
        cargo = None
        salario = None
        biografia = None
        departamento_id = None
        biblioteca_id = None

        if tipo == "FUNCIONARIO":
            cargo = choice(cargos_biblioteca)
            salario = randint(2000, 10000)
            departamento_id = randint(1,5)
        elif tipo == "AUTOR":
            biografia = choice(biografias)

        pessoa = Pessoa(
            id_pessoa=i,
            nome=nome,
            cpf=cpf,
            cep=cep,
            estado=estado,
            cidade=cidade,
            bairro=bairro,
            rua=rua,
            numero=numero,
            email=email,
            tipo_pessoa=tipo,
            data_cadastro=str(data_cadastro),
            status_conta=status,
            cargo=cargo,
            data_admissao=str(data_admissao),
            salario=salario,
            departamento_id=departamento_id,
            biblioteca_id=biblioteca_id,
            data_nascimento=str(data_nascimento),
            biografia=biografia,
            nacionalidade=nacionalidade,
            endereco=endereco
        )

        pessoas.append(pessoa)
    return pessoas

def make_library() -> list:
    bibliotecas = [
        "Biblioteca Central de São Paulo",
        "Biblioteca Monteiro Lobato",
        "Biblioteca do Saber",
        "Biblioteca Paulo Freire",
        "Biblioteca Luz do Conhecimento",
        "Biblioteca Machado de Assis",
        "Biblioteca Tecnológica da FEI",
        "Biblioteca Cultural do Brasil",
        "Biblioteca José de Alencar",
        "Biblioteca Digital Horizonte"
    ]

    lista_bibliotecas = []

    for l in bibliotecas:
        id_biblioteca = bibliotecas.index(l) + 1
        email = fake.email()
        telefone = fake.phone_number()
        endereco = fake.address()
        nome = l
        biblioteca = Biblioteca(id_biblioteca=id_biblioteca, nome=nome, telefone=telefone,
                                endereco=endereco, email=email)
        lista_bibliotecas.append(biblioteca)
        id_biblioteca = id_biblioteca +1
    
    return lista_bibliotecas

def make_publisher() -> None:
    editoras = [
    "Editora Companhia das Letras",
    "Editora Record",
    "Editora Rocco",
    "Editora Intrínseca",
    "Editora Saraiva",
    "Editora Objetiva",
    "Editora Globo Livros",
    "Editora Moderna",
    "Editora Atlas",
    "Editora Sextante"
    ]   

    lista_editora = []
    for e in editoras:
        nome = e
        cnpj = fake.cnpj()
        endereco = fake.address()
        telefone = fake.phone_number()
        email = fake.email()
        editora = Editora(nome=nome,cnpj=cnpj, endereco=endereco, telefone=telefone, email=email)
        lista_editora.append(editora)

    return lista_editora

def make_books() -> None:
    books = [
        "As Sombras de Aurora",
        "O Último Guardião do Tempo",
        "Entre Estrelas e Tempestades",
        "A Casa das Vozes Perdidas",
        "O Jardim dos Relógios Quebrados",
        "Memórias de Um Mundo Submerso",
        "A Canção dos Ventos Antigos",
        "O Herdeiro das Cinzas",
        "Ecos de Um Futuro Esquecido",
        "O Segredo do Farol Silencioso"
    ]

    lista_livros = []

    for b in books:
        editora_id = randint(1,10)
        titulo = b
        biblioteca_id = randint(1,10)
        ano_publicacao = str(fake.date_between(start_date, end_date))
        isbn = randint(1111111111111,9999999999999)
        autor = fake.name()
        livro = Livro(editora_id=editora_id, titulo=titulo, biblioteca_id=biblioteca_id,
                      ano_pubicacao=ano_publicacao, isbn=isbn, autor=autor)
        lista_livros.append(livro)
    
    return lista_livros



if __name__ == "__main__":
    pessoas = make_people(5)
    print("ok")
    bibliotecas = make_books()
    print(bibliotecas[0].titulo)
    print(bibliotecas[-1].titulo)
    