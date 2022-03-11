from random import randint
from time import sleep


def sorteia():
    print('Sorteando os 5 valores da lista: ', end='', flush=True)
    for num in range(0, 5):
        n = randint(0, 100)
        sleep(0.5)
        print(f'{n} ', end='', flush=True)
        lista.append(n)
    print('PRONTO!')


def somaPar():
    s = 0
    print(f'Somando os números pares de {lista}, temos: ', end='')
    for num in lista:
        if num % 2 == 0:
            s += num
    print(s)


lista = list()
sorteia()
somaPar()
