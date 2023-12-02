def valida_cpf():
    cpf = '43067823472'
    cpf = list(cpf)
    print(cpf)


    """Removendo o penúltimo"""
    lista1 = cpf.copy()  # Criar uma cópia independente
    lista1.pop(8)
    print(lista1)

    """Removendo o último"""
    lista2 = cpf.copy()  # Criar outra cópia independente
    lista2.pop(9)
    print(lista2)



valida_cpf()

def todos_digitos(lista):
    for valor in lista:
        if not valor.isdigit():
            return False
    return True