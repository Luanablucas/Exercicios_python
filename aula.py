import os

def exibir_nome_do_programa():
    print('Bem-vindo ao sistema de restaurantes!')

def exibir_menu():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante')
    print('3 - Ativar restaurante')
    print('4 - Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando aplicação...')  

def opcoes_invalidas():
    print('Opção inválida! Tente novamente.\n')
    input('Pressione Enter para voltar ao menu')
    main()

def escolher_opcao():  
    try:
        opcao_escolhida = int(input('Digite a opção desejada: '))
        print(f'Opção escolhida: {opcao_escolhida}')

        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:  
            finalizar_app()
        else: 
            print('Opção inválida! Tente novamente.')
            escolher_opcao()
    except:
        opcoes_invalidas()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()