def exibir_menu():
    global opc
    print(30*"~-")
    print(f"""
    1 - Cadastrar
    2 - Exibir Frase
    3 - Sair
    """)
    print(33 * "~-")
    x = True
    while x:
        opc = int(input(f'Escolha um item do menu: '))
        if 1 <= opc <= 3:
            x = False
            print(33 * "~-")
        else:
            print(f'digito incorreto! Digite um numero entre 1 e 2 ou 3 para prosseguir: ')
            print(33 * "~-")
    return opc



