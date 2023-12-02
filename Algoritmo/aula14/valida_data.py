from datetime import datetime


def valida_data():
    data_nascimento = str(input("Insira a data do seu nascimento: "))
    # Verifica o formato da string de data
    if len(data_nascimento) != 10 or not data_nascimento[0:2].isdigit() or not data_nascimento[3:5].isdigit() or not data_nascimento[6:].isdigit() or data_nascimento[2] != '/' or data_nascimento[5] != '/':
        print('Formato de data inválido. Use o formato DD/MM/AAAA')
        return valida_data()


    # Extrai ano, mês e dia
    dia = int(data_nascimento[0:2])
    mes = int(data_nascimento[3:5])
    ano = int(data_nascimento[6:])

    hoje = datetime.now().date()
    data_nasc = datetime(ano, mes, dia).date()
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
    if idade < 18:
        return False
    else:
        return True
