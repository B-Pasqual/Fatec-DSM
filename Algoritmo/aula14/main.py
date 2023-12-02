import random
from exibir_menu import exibir_menu
from valida_cpf import valida_cpf
from valida_data import valida_data

array_mensagens = ['A persistência realiza o impossível', 'Seus sonhos não precisam de plateia, eles só precisam de você', 'A persistência é o caminho do êxito', 'No meio da dificuldade e encontra-se a oportunidade']



def script_principal():
    option = exibir_menu()
    if option == 1: 
        nome = input('Digite o nome a ser cadastrado: ')
        input('Digite o sobrenome: ')
        (input('Digite a renda bruta: '))
        valida_cpf()
        if valida_data():
            print('Usuário cadastrado com sucesso')
        else:
            print('Não foi possível cadastrar, usuário menor de idade')
    if option == 2:
        print(random.choice(array_mensagens))
    if option == 3:
        print('Bye bye')
      

script_principal()