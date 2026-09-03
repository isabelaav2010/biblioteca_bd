import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#apaga a tabela usuarios
conn.execute("DROP TABLE IF EXISTS usuarios")

#cria a tabela usuarios
conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome TEXT NOT NULL)")

#inserindo os registros na tabela usuarios
conn.executemany("INSERT INTO usuarios(nome) VALUES(?)",
                 [("Bob",), ("Sam",), ("Frodo",)])

#confirmando a criação e os inserts da tabela usuarios.
conn.commit()