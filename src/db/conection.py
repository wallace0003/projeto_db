import os
from dotenv import load_dotenv
from supabase import create_client, Client
from src.script.make_data import make_people, make_library
from src.models.departamento import Departamento

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def add_people(n_rows:int) -> None:
    pessoas = make_people(n_rows)

    for p in pessoas:
        response = (
            supabase.table("pessoas")
            .insert({
                "id_pessoa": p.id_pessoa,
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

    print("🎉 Inserção concluída com sucesso!")

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

def create_biblioteca() -> None:
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
        print("❌ Erro ao criar departamentos:", e)

if __name__ == "__main__":
    create_biblioteca()
