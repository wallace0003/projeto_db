import os
from dotenv import load_dotenv
from supabase import create_client, Client
from src.script.make_data import make_people

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def add_people(n_rows):
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



if __name__ == "__main__":
    add_people(100)
