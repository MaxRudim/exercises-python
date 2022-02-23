from random import randint

n = randint(1, 100)

print(f'O número escolhido foi: {n}')

if n % 2 == 0:
    print('O número escolhido é PAR!')
else:
    print('O número escolhido é  IMPAR!')
