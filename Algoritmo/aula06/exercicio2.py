def calculaDesconto():
    valorDaCompra = float(input('Digite o valor da sua compra'))
    
    if valorDaCompra <= 1000:
        print(f'Valor do desconto: R$ {valorDaCompra* 0.1}')
    elif valorDaCompra > 1000 and valorDaCompra <= 5000:
        print(f'Valor do desconto: R$ {valorDaCompra * 0.2}')
    else:
        print(f'Valor do desconto: R$ {valorDaCompra*0.3}')
        
calculaDesconto()