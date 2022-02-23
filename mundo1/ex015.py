alugado = int(input('Por quantos dias alugou o carro? '))
rodou = float(input('Por quantos kms rodou com o carro? '))

print(f'O total a pagar é de: \
R${(alugado * 60) + (rodou * 0.15)}')
