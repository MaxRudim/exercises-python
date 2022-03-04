dados = dict()
all_data = list()

while True:
    dados['jogador'] = str(input('Nome do jogador: ')).capitalize()

    dados['gols'] = []

    games = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))

    for num in range(1, games+1):
        gol = int(input(f'Quantos gols na partida {num}? '))

        dados['gols'].append(gol)

    dados['total'] = sum(dados['gols'])

    all_data.append(dados.copy())

    while True:

        go_on = str(input('Voce deseja continuar? [S/N] ')).strip().upper()[0]

        if go_on in 'SN':
            break

        print('ERRO! Responda apenas S ou N.')

    if go_on == 'N':
        break


print('-=' * 20)

print(f'{"Cod.":<4}  {"Nome":<10}{"Gols":<8}{"Total":>8}')

for index, element in enumerate(all_data):

    print(f'{index}     {element["jogador"]}       \
{element["gols"]}       {element["total"]}')

print('-=' * 20)

print('')

while True:
    n = int(input('Digite o Cod. do jogador que \
deseja pesquisar (999 para parar): '))

    if 0 <= n < len(all_data):
        print('')

        print(f'Levantamento do jogador: {all_data[n]["jogador"]}')

        for index, element in enumerate(all_data[n]['gols']):

            print(f' => Na partida {index + 1}, fez {element} gols.')

    elif n == 999:
        break
    else:
        print('Jogador não encontrado, digite o jogador \
correspondente ao seu Cod. mostrado na tabela acima.')
