dados = dict()

dados['jogador'] = str(input('Nome do jogador: '))
dados['gols'] = []
games = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))

for num in range(1, games+1):
    gol = int(input(f'Quantos gols na partida {num}? '))
    dados['gols'].append(gol)

dados['total'] = sum(dados['gols'])
print('-=' * 20)
print(dados)
print('-=' * 20)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 20)

print(f'O jogador {dados["jogador"]} jogou {games} partidas.')

for index, element in enumerate(dados['gols']):
    print(f' => Na partida {index + 1}, fez {element} gols.')

print(f'Foi um total de {dados["total"]} gols.')
