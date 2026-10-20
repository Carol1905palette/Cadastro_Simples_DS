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
    if (opcao == 1 ) :
        print("==========================")
        print("=====Tela de Cadastro=====")
        print("==========================")
    #se digitar 2, abre a tela de login
    elif("opcao == 2 ") : 
        print("=======================")
        print("=====Tela de Login=====")
        print("=======================")
    #Se digitar 3, sai da execução
    elif(opcao == 3):
        print("Voc está saindo do cadastro, até mais!")
        break
    #Se não for nem 1,2 ou 3 mostrar erro e repetir código 
    else:
        print("Valor digitado, inválido, use apenas números inteiros do menu")
    