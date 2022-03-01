from random import randint

print('Tente adivinhar o número pensado pelo computador.')
n = int(input('De 1 a 10, digite um número: '))

bot = randint(1, 10)
count = 1

while n != bot:
    count += 1
    n = int(input('Que pena, você errou. Tente outro número: '))

print(f'Parabéns, após {count} tentativas, você acertou.')
