from random import randint

print('-=' * 50)

print('Sorteador de números para inserir em tuplas')

print('-=' * 50)

lista = list()

for n in range(0, 6):
    num = randint(0, 100)
    lista.append(num)

tupla = tuple(lista)

print('')
print(f'A tupla é: {tupla}')

print(f'O maior valor da tupla é: {max(tupla)}')

print(f'O menor valor da tupla é: {min(tupla)}')
