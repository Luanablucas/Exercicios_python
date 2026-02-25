import os

restaurantes = [{"nome": "Churrascaria Hotel", "categoria": "Churrascaria", "ativo": True},
                {"nome": "Pizzaria Bella", "categoria": "Italiano", "ativo": False},
                {"nome": "Sushi House", "categoria": "Japonês", "ativo": False}]

def exibir_nome_do_programa():
    print('Bem-vindo ao sistema de restaurantes!')

def exibir_menu():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante')
    print('3 - Ativar restaurante')
    print('4 - Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrando o programa...')

def voltar_ao_menu():
    input('\nPressione Enter para voltar ao menu principal')
    main()

def opcoes_invalidas():
    print('Opção inválida! Tente novamente.\n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')        
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'Restaurante "{nome_restaurante}" cadastrado com sucesso!\n')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes cadastrados')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} |  {categoria} | {ativo}')
         
    voltar_ao_menu()

def escolher_opcao():  
    try:
        opcao_escolhida = int(input('Digite a opção desejada: '))
        print(f'Opção escolhida: {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
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