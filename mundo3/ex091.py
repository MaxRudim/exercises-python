from random import randint

game = dict()

for num in range(1, 5):
    game[f"Jogador nº {num}"] = randint(1, 6)

print('')

print('Valores sorteados:')

for k, v in game.items():
    print(f'O {k} tirou {v}')

print('')

print('Ranking dos jogadores:')

sorted_game = sorted(game.items(), key=lambda x: x[1], reverse=True)

for index, element in enumerate(sorted_game):
    print(f'{index + 1}º Lugar: {element[0]}, com {element[1]} pontos.')
