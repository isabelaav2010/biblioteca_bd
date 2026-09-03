# biblioteca_bd - Aplicação com Banco de Dados

Implementação do exemplo clássico da Biblioteca salvando os dados em um banco de dados *sqlite*.

As tabelas do projeto são:

**usuarios**(*id, nome*)
**autor**(*id, nome*) 
**livros**(*id, titulo, ano_publicacao, edicao, disponivel, id_autor*)
**emprestimos**("id, usuario_id, data*)
**editora**(*id, nome*)
**emprestimos_livros**(*emprestimo_id, livro_id, data_devolucao*)
