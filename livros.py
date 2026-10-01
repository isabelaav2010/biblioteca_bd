def inclui_livros(con,titulo):
    con.executemany("INSERT INTO livros(titulo) VALUES(?)",
                 (titulo,))
    con.commit()

def get_id_livros(con,titulo):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

    cursor.execute(f"SELECT id FROM autores WHERES nome = '{titulo}'")
    resultado = cursor.fetch()
    
def lista_autores(con):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()



def lista_livros(con):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM usuarios")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"id: {linha['id']} - título: {linha['titulo']}")