def ehprimo (n):
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True

valor = int(input('Digite um valor: '))
if ehprimo(valor):
    print('O valor é primo')
else:
    print('O valor não é primo')