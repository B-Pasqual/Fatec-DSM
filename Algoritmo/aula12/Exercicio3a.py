dicionario = {}
idades = 0

for item in range(5):
    sobrenome = input('Digite o sobrenome')
    idade = int(input('Digite a idade'))
    dicionario[sobrenome] = idade
    idades += idade

print(f"A média das idades é: {idades/len(dicionario)}")
print('Os nomes que correspondem é')

for sobrenome, idade in dicionario.items():
    if idade > idades / len(dicionario):
        print(f"{sobrenome} idade: {idade}")

