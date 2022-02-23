salario = float(input('Digite o seu salário sem pontos ou virgulas: R$ '))

if salario > 1250.0:
    aumento = salario + (salario * 10/100)
    print(f'Parabéns, seu salário passou a ser de: R$ {round(aumento, 2)}0')
else:
    aumento = salario + (salario * 15/100)
    print(f'Parabéns, seu salário passou a ser de: R$ {round(aumento, 2)}0')
