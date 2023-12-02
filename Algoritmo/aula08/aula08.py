""" Exercício 1 (mostrar nome completo) """
"""


primeiroNome = input('Digite o primeiro nome \n');
segundoNome = input('Digite o sobrenome \n');
ultimoNome = input('Digite o último nome \n');

print(f'{primeiroNome} {segundoNome} {ultimoNome}')
"""

"""
Exercício 2 - mostrar a data em um formato diferente

data = input('Digite a data no formato dd/mm/aaaa ')
[dia, mes, ano] = [data[0:2], data[3:5], data[6:11]]
print(f'{ano}{mes}{dia}')

"""
""" Programa para colocar ponto e vírgula """

""" Formatar número  """
""" 
while True:
    valor = input("Digite os números: ")
    if valor.isnumeric() and len(valor) == 9:
        break;

    if len(valor) != 9:
        print('Tem que ter 9 dígitos!!')
    else:
        print('Digite apenas números!!')

novo_valor = f'{valor[0]}.{valor[1:4]}.{valor[4:7]},{valor[7:9]}'
print(novo_valor)

"""

""" Contador de vogais """

"""

frase = input('Digite a sua frase: ')
quantidade = 0
vogais = 'aeiouAEIOU'

for letra in frase:
    if letra in vogais:
        quantidade += 1

print(f'O número de vogais na string é: {quantidade}')

"""

"""

frase = input('Digite a sua frase: ').lower()
palavra = input('Digite a palavra a ser procurada').lower()

print(frase.count(palavra))

"""

palavra = input('Digite a palavra: ').lower()
inversa = palavra[::-1]

if palavra == inversa:
    print(f'A palavra {palavra} é Palindroma ')
else:
    print(f'A palavra {palavra} não é Palindroma')