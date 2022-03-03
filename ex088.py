from time import sleep
from random import randint

games = int(input('Quantos jogos você quer que eu sorteie? '))

game = list()

print('')
print(f"{'-=' * 10} Sorteando {games} jogos {'-=' * 10}")

for element in range(1, (games + 1)):
    sleep(1)
    for num in range(0, 6):
        number = randint(1, 60)
        game.append(number)

    print(f'Jogo {element}: {game}')

    game.clear()

print(f"{'-=' * 10} < BOA SORTE! > {'-=' * 10}")
