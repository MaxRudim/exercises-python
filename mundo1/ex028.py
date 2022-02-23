from random import randint

print('Tente adivinhar o número pensado pelo computador.')
n = int(input('De 0 a 5 digite um número: '))

r_n = randint(1, 5)

print(f'Voce digitou o número: {n} enquanto \
o computador pensou o número: {r_n}')
if n == r_n:
    print('Parabéns, você acertou.')
else:
    print('Que pena, voce errou.')
