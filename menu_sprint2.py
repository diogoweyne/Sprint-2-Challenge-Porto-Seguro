usuarios = []

# Def da função para cadastro de usuário e a coleta de dados para cadastro
def cadastrar_usuario():
    nome = input("Digite seu nome de usuário: ")
    email = input("Digite seu email: ")
    senha = input("Crie uma senha: ")
    endereco = input("Digite seu endereço: ")
    usuarios.append({'nome': nome, 'email': email, 'senha': senha, 'endereco': endereco, 'servicos': []})
    print("Usuário cadastrado com sucesso!")

#Def da função de solicitação de serviço e a coleta de dados para cadastro
def solicitar_servico():
    nome_usuario_servico = input("Digite o nome do usuário que está cadastrando o serviço: ")
    for usuario in usuarios:
        if usuario['nome'] == nome_usuario_servico:
            id_servico = input("Digite o ID do serviço: ")
            localizacao = input("Digite a localização do serviço: ")
            tipo_servico = input("Digite o tipo do serviço: ")
            descricao = input("Digite a descrição do serviço: ")
            categoria = input("Digite a categoria do serviço: ")

            usuario['servicos'].append({'id_servico': id_servico, 'localizacao': localizacao, 'tipo_servico': tipo_servico, 'descricao': descricao, 'categoria': categoria})
            print("Serviço cadastrado com sucesso!")
            return
    print("Usuário não encontrado. Por favor, cadastre o usuário antes de cadastrar o serviço.")

#Def da função para mostrar usuários cadastrados
def mostrar_usuarios_cadastrados():
    if usuarios:
        print("LISTA DE USUÁRIOS CADASTRADOS:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, Email: {usuario['email']}, Endereço: {usuario['endereco']}")
            if usuario['servicos']:
                print("Serviços solicitados:")
                for servico in usuario['servicos']:
                    print(f"Tipo de serviço: {servico['tipo_servico']}")
                    print(f"Descrição: {servico['descricao']}")
                    print(f"Categoria: {servico['categoria']}")
                    print(f"Localização: {servico['localizacao']}")
    else:
        print("Nenhum usuário cadastrado.")

#Menu com as opções que vão aparecer para o usuário escolher
def menu():
    while True:
        print("MENU")
        print("1. Cadastro de novo usuário")
        print("2. Solicitar serviço")
        print("3. Mostrar os usuários cadastrados")
        print("4. Sair")
        print("5. Como posso ajudar?")
        opcao = input("Escolha uma opção:")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            solicitar_servico()
        elif opcao == '3':
            mostrar_usuarios_cadastrados()
        elif opcao == '4':
            print("Programa finalizado.")

            break
#Nova função implementada para a segunda sprint, na qual oferece ajuda a um usuário por meio de um e-mail
        elif opcao == '5':
            print("Como posso ajudar?")
            print("Caso possua alguma dúvida, mande um e-mail para oztech@exemplo.com")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()