print('-=' * 40)

print('Tabuada com loop + break')

print('-=' * 40)

while True:
    n = int(input('\nDigite um número inteiro positivo para ver sua tabuada,\
se for um número negativo o progama encerra: '))
    if n < 0:
        break
    for num in range(1, 11):
        print(f'{num} x {n} = {num * n}')

print('Programa encerrado!')
