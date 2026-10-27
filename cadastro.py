    #Variaveis para cadastro
nome = ""
idade = "" 
mksenha = ""

 #Variaveis de login
login_usuário = ""
login_senha = ""

#Variaveis de controle
controle_cadastro = ""

 #Apenas tela de Visualizacao
while True:
    print("===================")
    print("Sistema de Cadastro")
    print("===================")

    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao = input("Escolha uma opcão: ")
        #Funcionalidades
        #Se o usuario digitar o valor 1, vai ser exibido
        # a ação 
    if (opcao == "1" ) :
           while controle_cadastro != "1" :
            print("==========================")
            print("=====Tela de Cadastro=====")
            print("==========================")
            nome =input("Digite o seu nome: ")
            idade =input("Digite a sua idade:")
            usuario =input("Digite seu usuário: ")
            senha =input("Digite sua senha: ")

            catrole_cadrasro = input("\nVocê deseja voltar para a tela anterior ?\n 1)- Voltar para o menu anterior;\n Digite qualquer tecla para refazer o cadastro;\n ")

            if(controle_cadastro =="1"):
                 print("\n Cadastro realizado!\n")
            else:
                print("Valor diditado inválido, faça o cadastro novamente")
     #se digitar 2, abre a tela de login
    elif(opcao == "2") : 
        print("=======================")
        print("=====Tela de Login=====")
        print("=======================")
        login_usuário = input(" Digite o usuário cadastrado: ")
        login_senha = input("Digite a senha: ")

             #Processamento de usuário e senha 
        if login_usuario == usuario and login_senha == senha :
            while True:
                print("\nLogin realizado com sucesso!\n")
                print("Bem vindo,", nome )
                print("\n=====Area de Usuário=====\n")
                print("1 - Ver os dados cadastrados")
                print("2- Voltar para o meu anterior")

                usuário_opcao = input("\nEscolha uma das opções do menu acima: ")

                if (usuário_opcao == "1"):
                    print("\n=======================")
                    print("====Dados Cadastrados====")
                    print("=======================\n")
                    #Mostrar dados do usuário:
                    print("Nome de usuário: ", nome)
                    print("Idade do usuário: ", idade)
                    print("Senha do usuário: ", senha)
                    print("Nome de cadastro: ", usuario)
                elif(usuário_opcao == "2"):
                    print("\n Você está voltando para o menu anterior!")
            #Se não tiver correto entra no caso abaixo
        else:
            print("\nUsuário  ou senha incorretos\n")
         #Se digitar 3, sai da execução 
    elif (opcao == "3"):
        print("Você está saindo do cadastro, até mais!")
        break
    #Se não for nem 1,2 ou 3 mostrar erro e repetir código 
    else:
        print("Valor digitado, inválido, use apenas números inteiros do menu")
         
            