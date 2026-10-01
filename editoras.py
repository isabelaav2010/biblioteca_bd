def inclui_editoras(con, nome):
    con.execute("INSERT INTO editoras(nome) VALUES(?)",
                 (nome,))
    con.commit()
    
def lista_editoras(con, nome):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

def get_id_editoras(con, nome_editora):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

    cursor.execute(f"SELECT id FROM autores WHERES nome = '{nome_editora}'")
    resultado = cursor.fetch()
    
def lista_autores(con):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

#executa o sql
    cursor.execute("SELECT * FROM editoras")

#pega os registros e guarda na variável resultados
    resultados = cursor.fetchall()

#percorre os registros que retornaram
    for linha in resultados:
        print(f"id: {linha['id']} | nome: {linha['nome_editora']}")
    #print(f"id: {linha[0]} | nome: {linha[1]}")