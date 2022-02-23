km = int(input('Digite quantos kms você viajará: '))

if 200 >= km:
    valor = float(km * 0.50)
    print(f'Voce terá que pagar: R$ {round(valor, 2)}0')
else:
    valor = float(km * 0.45)
    print(f'Você terá que pagar: R$ {round(valor, 2)}')
