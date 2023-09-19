def ehDivisivel():
    numero = float(input('Digite um número:'))
    
    if numero % 3 == 0 and numero % 5 == 0:
        print('O numero foi divisivel por ambos')
    else:
        print('O numero nao foi divisivel')
        
ehDivisivel()
