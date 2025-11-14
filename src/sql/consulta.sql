# 1º Consulta
SELECT 
  l.titulo,
  e.nome as editora,
  COUNT(emp.id_emprestimo) as total_emprestimos
FROM livros l 
JOIN editoras e ON l.editora_id = e.id_editora
LEFT JOIN emprestimos emp ON l.id_livro = emp.livro_id
WHERE l.ano_publicacao >= 2000
GROUP BY l.id_livro, l.titulo, e.nome
ORDER BY total_emprestimos DESC, l.titulo;

# 2º Consulta
SELECT 
    p.nome as usuario,
    p.email,
    COUNT(emp.id_emprestimo) as total_emprestimos,
    COUNT(CASE WHEN emp.status = 'EM_ATRASO' THEN 1 END) as emprestimos_atraso,
    COUNT(CASE WHEN emp.status = 'ATIVO' THEN 1 END) as emprestimos_ativos,
    ROUND(AVG(emp.data_devolucao - emp.data_emprestimo)::numeric, 1) as media_dias_emprestimo
FROM pessoas p
JOIN emprestimos emp ON p.id_pessoa = emp.usuario_id
JOIN livros l ON emp.livro_id = l.id_livro
WHERE p.tipo_pessoa = 'USUARIO'
GROUP BY p.id_pessoa, p.nome, p.email
HAVING COUNT(emp.id_emprestimo) > 0  
ORDER BY total_emprestimos DESC;

# 3º Consulta
SELECT 
    autor.nome as autor,
    autor.nacionalidade,
    cat.categoria,
    COUNT(DISTINCT la.livro_id) as total_livros_categoria,
    COUNT(emp.id_emprestimo) as total_emprestimos,
    (SELECT COUNT(*) 
     FROM livro_autor la2 
     JOIN livros l2 ON la2.livro_id = l2.id_livro 
     WHERE la2.autor_id = autor.id_pessoa) as total_livros_autor
FROM pessoas autor
JOIN livro_autor la ON autor.id_pessoa = la.autor_id
JOIN livros l ON la.livro_id = l.id_livro
JOIN livro_categorias cat ON l.id_livro = cat.livro_id
LEFT JOIN emprestimos emp ON l.id_livro = emp.livro_id
WHERE autor.tipo_pessoa = 'AUTOR'
GROUP BY autor.id_pessoa, autor.nome, autor.nacionalidade, cat.categoria
HAVING COUNT(emp.id_emprestimo) > 0
ORDER BY total_emprestimos DESC, autor.nome, cat.categoria;