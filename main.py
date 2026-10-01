import sqlite3 as sqlite
from util import limpa_tela
from usuarios import inclui_usuario, lista_usuarios
from autores import inclui_autores, get_id_autor, lista_autores
from editoras import inclui_editoras, lista_editoras, get_id_editoras
from livros import inclui_livros, lista_livros, get_id_livros
from emprestimos import inclui_emprestimos, lista_emprestimos

#abre a conexão com o banco
conn = sqlite.connect("biblioteca.db")
conn.row_factory = sqlite.Row

def menu_usuarios():
    while(True):
        limpa_tela()
        print("-----Menu usuários-----")
        print("[1]-Incluir\n[2]-Listar\n[3]Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            nome = input("Nome de usuário: ")
            inclui_usuario(conn, nome)
        elif (opcao == '2'):
            lista_usuarios(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == 3):
            limpa_tela()
            break
        else:
            print("Opção inválida! Digite uma tecla para continuar...")


def menu_autores():
    while(True):
        limpa_tela()
        print("-----Menu autores -----")
        print("[1]-Incluir\n[2]-Listar\n[3]Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            nome = input("Nome do autor: ")
            inclui_autores(conn, nome)
        elif (opcao == '2'):
            lista_autores(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == 3):
            limpa_tela()
            break
        else:
            print("Opção inválida! Digite uma tecla para continuar...")

def menu_editoras():
    while(True):
        limpa_tela()
        print("-----Menu editoras -----")
        print("[1]-Incluir\n[2]-Listar\n[3]Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            nome_editora = input("Nome da editora: ")
            inclui_editoras(conn, nome_editora)
        elif (opcao == '2'):
            lista_editoras(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == 3):
            limpa_tela()
            break
        else:
            print("Opção inválida! Digite uma tecla para continuar...")

def menu_livros():
    while(True):
        limpa_tela()
        print("-----Menu livros-----")
        print("[1]-Incluir\n[2]-Listar\n[3]Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            titulo = input("Título do livro: ")
            inclui_livros(conn, titulo)
        elif (opcao == '2'):
            lista_livros(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == 3):
            limpa_tela()
            break
        else:
            print("Opção inválida! Digite uma tecla para continuar...")

while(True):
    limpa_tela()
    print("------Sistema da Biblioteca------") 
    print("Digite:\n[1]-Usuários\n[2]-Autores\n[3]-Editoras\n[4]-Livros")
    opcao = input("Digite a opção: ")

    if (opcao =='1'):
        menu_usuarios()
    if (opcao == '2'):
        menu_autores()
    if (opcao == '3'):
        menu_editoras
    if (opcao == '4'):
        menu_livros()

    else:
        break
#fecha a conexão
conn.close()