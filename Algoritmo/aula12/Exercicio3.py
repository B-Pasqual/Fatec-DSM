dicionario = {}
maior = 0;

for item in range(5):
    sobrenome = input('Digite o sobrenome')
    idade = int(input('Digite a idade'))
    dicionario[sobrenome] = idade
    if maior == 0:
        maior = (sobrenome, idade)
    else:
        if maior[1] < idade:
            maior = (sobrenome, idade)

print(maior)
print(f"O sobrenome com a maior idade é: {maior[0]} com a idade de: {maior[1]}")






