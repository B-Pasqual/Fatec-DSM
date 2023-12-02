def ehprimo (n):
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True

def checaPrimos():
    valor = int(input('Digite um valor'))
    quantidadePrimos = 0
    if valor <= 0:
        checaPrimos()
    for i in range(valor + 1):

        if ehprimo(i) and i != 0:
            quantidadePrimos += 1

    print(quantidadePrimos)
checaPrimos()