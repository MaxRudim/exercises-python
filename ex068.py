from random import randint

print('-=' * 40)

print('Jogo de par ou ímpar com o computador')

print('-=' * 40)

options = "PARIMPAR"
victory = 0

while True:
    opt = str(input('\nDigite sua escolha \
entre PAR ou IMPAR: ')).strip().upper()
    while opt not in options:
        opt = str(input('\nDigite exatamente sua \
escolha entre PAR ou IMPAR: ')).strip().upper()
    num = int(input('\nDigite um número inteiro e positivo qualquer: '))
    bot = randint(1, 100)

    if (num + bot) % 2 == 0:
        print('\nParabéns, você venceu uma rodada.')
        victory += 1
    else:
        print('\nQue pena, voce perdeu.')
        break

print(f'\nVocê teve um total de {victory} vitórias consecutivas. \
Obrigado por jogar.')
