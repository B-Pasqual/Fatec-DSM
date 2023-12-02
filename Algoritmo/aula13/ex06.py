def calculaSegundos(horas, minutos, segundos):
    return f'A quantidade em segundos é: {((horas*60*60) + (60*minutos) + segundos)}'

print(calculaSegundos(int(input('Digite a quantidade de horas: ')),int(input('Digite a quantidade de minutos: ')),int(input('Digite a quantidade de segundos: '))))