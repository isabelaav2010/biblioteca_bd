def inclui_emprestimos(con, usuarios, livros):
    sql_insert = f"INSERT INTO emprestimos (usuario_id) VALUES "
