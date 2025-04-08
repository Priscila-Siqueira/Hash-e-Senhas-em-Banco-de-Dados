from banco_de_dados import criar_banco, fechar_banco
from funcoes import cadastrar_senha, validar_senha, pesquisar_hash

def main():
    # Conecta (ou cria) o banco de dados e obtém cursor
    conexao, cursor = criar_banco()

    while True:
        print("\n--- MENU ---")
        print("1) Cadastro")
        print("2) Login")
        print("3) Pesquisa de Hash")
        print("4) Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_senha(cursor, conexao)
        elif opcao == "2":
            validar_senha(cursor, conexao)
        elif opcao == "3":
            pesquisar_hash(cursor)
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

    # Fecha a conexão com o banco antes de encerrar
    fechar_banco(conexao)

if __name__ == "__main__":
    main()