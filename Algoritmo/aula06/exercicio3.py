def quantas_latas():
    largura = float(input('Digite a largura do comodo: '))
    comprimento = float(input('Digite o comprimento do comodo: '))
    capacidade_lata = float(input('Qual a capacidade da lata que será utilizada: '))

    area_para_pintar = ((4 * comprimento) - (0.8 * 2.1))
    litros_necessarios = area_para_pintar / 3
    soma_litros = 0
    quantidade_latas = 0

    while (soma_litros < litros_necessarios):
        soma_litros = soma_litros + capacidade_lata
        quantidade_latas = quantidade_latas + 1

    print(f'\nárea para se pintar: {area_para_pintar} m2')
    print(f'tamanho da lata: {capacidade_lata} litros')
    print(f'latas necessárias: {quantidade_latas}')


quantas_latas()