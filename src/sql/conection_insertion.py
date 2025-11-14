import os
from dotenv import load_dotenv
from supabase import create_client, Client
from src.script.make_data import make_people, make_library, make_publisher, make_books 
from src.script.make_data import make_categories, make_book_author, make_loan
from src.models.departamento import Departamento

#para rodar o codigo utiliza o comando: "python3 -m src.sql.conection_insertion"

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def add_people(n_rows:int, nomes_tipo_pessoas: dict[str, list[str]] | None = None) -> None:
    pessoas = make_people(n_rows, nomes_tipo_pessoas)

    for p in pessoas:
        response = (
            supabase.table("pessoas")
            .insert({
                "nome": p.nome,
                "cpf": p.cpf,
                "email": p.email,
                "tipo_pessoa": p.tipo_pessoa,
                "data_cadastro": p.data_cadastro,
                "status_conta": p.status_conta,
                "cargo": p.cargo,
                "data_admissao": p.data_admissao,
                "salario": p.salario,
                "departamento_id": p.departamento_id,
                "biblioteca_id": p.departamento_id,
                "data_nascimento": p.data_nascimento,
                "biografia": p.biografia,
                "nacionalidade": p.nacionalidade,
                "endereco": p.endereco,
            })
            .execute()
        )
        print(f"✅ Pessoa {p.nome} inserida com sucesso!")

    print("✅ Inserção concluída com sucesso!")

def create_departament() -> None:
    departamentos = [
        Departamento(1, "Administração", 
                     "Gerencia geral e coordenação das atividades da biblioteca.", "Guilherme da Paz"),
        Departamento(2, "Aquisição", 
                     "Responsável pela seleção e compra de novos livros e materiais.", "Bruna da Mota"),
        Departamento(3, "Catalogação", 
                     "Cuida da organização, registro e indexação das obras.", "Sara Silveira"),
        Departamento(4, "Atendimento", 
                     "Auxilia leitores e gerencia empréstimos e devoluções.", "Antônio das Neves"),
        Departamento(5, "Tecnologia da Informação", 
                     "Mantém os sistemas e infraestrutura tecnológica da biblioteca.", "Sr. Samuel Correia")
    ]

    try:
        data = [{
            "id_departamento": d.id_departamento,
            "nome_departamento": d.nome_departamento,
            "descricao": d.descricao,
            "responsavel": d.responsavel
        } for d in departamentos]

        response = supabase.table("departamentos").insert(data).execute()
        print("✅ Departamentos criados com sucesso!")
        print(response)
    except Exception as e:
        print("❌ Erro ao criar departamentos:", e)

def create_library() -> None:
    bibliotecas = make_library()
    try:
        data =[{
            "nome":l.nome,
            "email":l.email,
            "endereco":l.endereco,
            "telefone":l.telefone,
        } for l in bibliotecas]

        response = supabase.table("bibliotecas").insert(data).execute()
        print("✅ Bibliotecas criadas com sucesso!")
        print(response)
    except Exception as e:
        print("❌ Erro ao criar Bibliotecas:", e)

def create_publisher() -> None:
    publishers = make_publisher()
    try:
        data =[{
            "nome":p.nome,
            "email":p.email,
            "endereco":p.endereco,
            "telefone":p.telefone,
            "cnpj":p.cnpj
        } for p in publishers]

        response = supabase.table("editoras").insert(data).execute()
        print("✅ Editoras criadas com sucesso!")
        print(response)
    except Exception as e:
        print("❌ Erro ao criar Editoras:", e)

def create_books() -> None:
    books = make_books()
    try:
        data =[{
            "biblioteca_id": b.biblioteca_id,
            "titulo": b.titulo,
            "editora_id": b.editora_id,
            "ano_publicacao": b.ano_pubicacao,
            "autor": b.autor,
            "isbn": b.isbn
        } for b in books]

        response = supabase.table("livros").insert(data).execute()
        print("✅ Livros criados com sucesso!")
        print(response)
    except Exception as e:
        print("❌ Erro ao criar livros:", e)

def create_categories() -> None:
    id_e_categorias = make_categories()
    try:
        data=[{
            "livro_id": chave,
            "categoria": valor
        } for chave, valor in id_e_categorias.items()]

        response = supabase.table("livro_categorias").insert(data).execute()
        print("✅ categorias criadas com sucesso!")
        print(response)
    except Exception as e:
        print("❌ Erro ao criar categorias:", e)

def create_book_author() -> None:
    livros_autores = make_book_author()
    try:
        data=[{
            "livro_id": livro_autor.livro_id,
            "autor_id": livro_autor.autor_id
        } for livro_autor in livros_autores]

        response = supabase.table("livro_autor").insert(data).execute()
        print("✅ livro e autores inseridos com sucesso!")
        print(response)
    except Exception as e:
        print("❌ Erro ao inserir livros e autores:", e)

def create_loan() -> None:
    emprestimos = make_loan(300)
    try:
        data=[{
            "data_emprestimo": str(emprestimo.data_emprestimo),
            "data_prevista_devolucao": str(emprestimo.data_prevista_devolucao),
            "data_devolucao": emprestimo.data_devolucao,
            "status": emprestimo.status,
            "usuario_id": emprestimo.usuario_id,
            "funcionario_id": emprestimo.funcionario_id,
            "livro_id": emprestimo.livro_id
        } for emprestimo in emprestimos]

        response = supabase.table("emprestimos").insert(data).execute()
        print("✅ Emprestimos inseridos com sucesso!")
        print(response)
    except Exception as e:
        print("❌ Erro ao inserir emprestimos", e)


if __name__ == "__main__":
    create_loan()
