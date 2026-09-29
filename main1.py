import sqlite3
from datetime import datetime

def cadastrar_usuario(nome, id):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    print("-- Cadastro de usuário --")
    nome = input("Digite o nome do usuário:")
    id = int(input("Digite o id do usuário:"))

    cursor.execute('''
        INSERT INTO usuarios (nome, id)
        VALUES (?, ?)
    ''', (nome, id))
    
    conn.commit()

def listar_usuario():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    conn.row_factory = sqlite.Row

    print("-- Lista de usuários --")
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    if not usuarios:
        print("Erro: usuário inexistente!")
    for usuario in usuarios:
        print(f"ID: {usuario['id']}| Nome: {usuario['nome']}")

    conn.commit()

def cadastrar_livro(id, titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")


    print("-- Cadastro de livro --")
    id = int(input("Digite o id do livro:"))
    titulo = input("Digite o título do livro:")
    autor_id = int(input("Digite o id do autor:"))
    editora_id = int(input("Digite o id da editora:"))
    ano_publicacao = int(input("Digite o ano de publicação:"))
    edicao = input("Digite a edição do livro:")
    disponivel = input("O livro está disponível? (sim/não):").lower() == 'sim' or 'não'
    if disponivel != 'sim' or "não":
        print("Erro: preencha com 'sim' ou 'não'! ")
    

    cursor.execute('''
        INSERT INTO livros (id, titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (id, titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel))
    
    conn.commit()

def listar_livro():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    conn.row_factory = sqlite.Row

    print("-- Lista de livros --")
    cursor.execute('SELECT * FROM usuarios' \
    'FROM livros, autores, editoras' \
    'WHERE livros.autor_id = autores.id' \
    'AND livros.editora_id = editora.id')
    livros = cursor.fetchall()
    if not livros:
        print("Erro: livro inexistente!")
    for livro in livros:
        print(f"ID: {livro['id']}| Título: {livro['titulo']}| Autor ID: {livro['autor_id']}|" \
              "Editora ID: {livro['editora_id']}| Ano de Publicação: {livro['ano_publicacao']}| Edição: {livro['edicao']}|" \
               "Disponível: {'Sim' if livro['disponivel'] else 'Não'}")

    conn.commit()

def cadastrar_autores():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor
