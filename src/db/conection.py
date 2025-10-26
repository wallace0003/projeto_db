import os
from dotenv import load_dotenv
from supabase import create_client, Client
from src.script.make_data import make_people

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def add_people():
    pessoas = make_people(3)

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
                "departamento_id": p.id_departamento if hasattr(p, "id_departamento") else None,
                "biblioteca_id": p.id_biblioteca if hasattr(p, "id_biblioteca") else None,
                "data_nascimento": p.data_nascimento,
                "biografia": p.biografia,
                "nacionalidade": p.nacionalidade if hasattr(p, "nacionalidade") else None,
                "endereco": p.endereco,
            })
            .execute()
        )
        
        print(f"✅ Pessoa {p.nome} inserida com sucesso!")

    print("🎉 Inserção concluída com sucesso!")



if __name__ == "__main__":
    add_people()
