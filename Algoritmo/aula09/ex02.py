lista = []
for i in range(6):
    lista.append(int(input(f'Digite o {i + 1} um número: ')))

print(f'O maior número é: {max(lista)}')
print(f'Ele está na posição {lista.index(max(lista))}')
