CREATE TABLE bibliotecas (
    id_biblioteca SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE departamentos (
    id_departamento SERIAL PRIMARY KEY,
    nome_departamento VARCHAR(50) NOT NULL,
    descricao TEXT,
    responsavel VARCHAR(100)
);

CREATE TABLE editoras (
    id_editora SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cnpj VARCHAR(18) UNIQUE,
    endereco VARCHAR(200),
    telefone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE pessoas (
    id_pessoa SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    endereco VARCHAR(200),
    email VARCHAR(100),
    tipo_pessoa VARCHAR(20) NOT NULL CHECK (tipo_pessoa IN ('USUARIO', 'FUNCIONARIO', 'AUTOR')),
    
    -- Usuário
    data_cadastro DATE,
    status_conta VARCHAR(20) CHECK (status_conta IN ('ATIVO', 'INATIVO', 'SUSPENSO')),
    
    -- Funcionário
    cargo VARCHAR(50),
    data_admissao DATE,
    salario DECIMAL(10,2),
    departamento_id INTEGER,
    biblioteca_id INTEGER,
    
    -- Autor
    nacionalidade VARCHAR(30),
    data_nascimento DATE,
    biografia TEXT,
    
    CONSTRAINT fk_funcionario_departamento 
        FOREIGN KEY (departamento_id) REFERENCES departamentos(id_departamento),
    CONSTRAINT fk_funcionario_biblioteca 
        FOREIGN KEY (biblioteca_id) REFERENCES bibliotecas(id_biblioteca)
);

CREATE TABLE livros (
    id_livro SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    ano_publicacao INTEGER,
    isbn VARCHAR(20),
    biblioteca_id INTEGER NOT NULL,
    editora_id INTEGER NOT NULL,
    FOREIGN KEY (biblioteca_id) REFERENCES bibliotecas(id_biblioteca),
    FOREIGN KEY (editora_id) REFERENCES editoras(id_editora)
);

CREATE TABLE livro_autor (
    livro_id INTEGER,
    autor_id INTEGER,
    PRIMARY KEY (livro_id, autor_id),
    FOREIGN KEY (livro_id) REFERENCES livros(id_livro) ON DELETE CASCADE,
    FOREIGN KEY (autor_id) REFERENCES pessoas(id_pessoa) ON DELETE CASCADE
);

CREATE TABLE livro_categorias (
    livro_id INTEGER,
    categoria VARCHAR(50),
    PRIMARY KEY (livro_id, categoria),
    FOREIGN KEY (livro_id) REFERENCES livros(id_livro) ON DELETE CASCADE
);

CREATE TABLE telefones_pessoas (
    pessoa_id INTEGER,
    numero_telefone VARCHAR(20),
    tipo VARCHAR(20) DEFAULT 'CELULAR',
    PRIMARY KEY (pessoa_id, numero_telefone),
    FOREIGN KEY (pessoa_id) REFERENCES pessoas(id_pessoa) ON DELETE CASCADE
);

CREATE TABLE emprestimos (
    id_emprestimo SERIAL PRIMARY KEY,
    data_emprestimo DATE NOT NULL,
    data_prevista_devolucao DATE NOT NULL,
    data_devolucao DATE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('ATIVO', 'CONCLUIDO', 'EM_ATRASO')),
    usuario_id INTEGER NOT NULL,
    funcionario_id INTEGER NOT NULL,
    livro_id INTEGER NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES pessoas(id_pessoa),
    FOREIGN KEY (funcionario_id) REFERENCES pessoas(id_pessoa),
    FOREIGN KEY (livro_id) REFERENCES livros(id_livro)
);