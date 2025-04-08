import hashlib

def cadastrar_senha(cursor, conexao):
    """
    Cadastra um novo usuário:
    - Lê email e senha do input,
    - Gera o hash da senha (SHA-256),
    - Insere no banco de dados.
    """
    email = input("Digite o email para cadastro: ")
    senha = input("Digite a senha: ")

    hash_senha = hashlib.sha256(senha.encode()).hexdigest()

    try:
        cursor.execute("INSERT INTO usuarios (email, hash_senha) VALUES (?, ?)", (email, hash_senha))
        conexao.commit()
        print("Cadastro realizado com sucesso!")
    except:
        print("ERRO: E-mail já cadastrado ou problema no banco.")

def validar_senha(cursor, conexao):
    """
    Faz o login (valida a senha):
    - Lê email e senha,
    - Compara o hash da senha digitada
      com o armazenado no banco.
    """
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    hash_senha = hashlib.sha256(senha.encode()).hexdigest()

    cursor.execute("SELECT hash_senha FROM usuarios WHERE email = ?", (email,))
    resultado = cursor.fetchone()

    if resultado:
        if resultado[0] == hash_senha:
            print("Login bem-sucedido!")
        else:
            print("Senha incorreta!")
    else:
        print("E-mail não encontrado!")

def pesquisar_hash(cursor):
    """
    Pesquisa o hash de um email no banco
    e exibe na tela se encontrado.
    """
    email = input("Digite o email para pesquisa: ")
    cursor.execute("SELECT hash_senha FROM usuarios WHERE email = ?", (email,))
    resultado = cursor.fetchone()

    if resultado:
        print(f"Hash da senha: {resultado[0]}")
    else:
        print("E-mail não encontrado!")