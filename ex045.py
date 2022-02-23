from random import randint
from time import sleep

choices = ['Pedra', 'Papel', 'Tesoura']
print('-=' * 40)
print('Jogo de jokenpô contra o computador')
print('-=' * 40)
print('''Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
print('-=' * 40)
player = int(input('Voce quer jogar 0 (pedra), 1 (papel) ou 2(tesoura)? '))
bot = randint(0, 2)

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

resultado = {
    'empataram': '\033[1;97mEMPATARAM\033[m',
    'ganhou': '\033[1;32mGANHOU\033[m',
    'perdeu': '\033[1;31mPERDEU\033[m'
    }

print('-=' * 40)
if player != 0 and player != 1 and player != 2:
    print('Jogada inválida. Digite apenas 0, 1 ou 2 conforme opções acima.')
elif bot == player:
    print(f'Você jogou {choices[player]} \
e o computador também jogou {choices[bot]}. Vocês {resultado["empataram"]}.')
elif bot == 0:
    if player == 1:
        print(f'Você jogou {choices[player]} \
e o computador jogou {choices[bot]}. Você {resultado["ganhou"]}.')
    else:
        print(f'Você jogou {choices[player]} \
e o computador jogou {choices[bot]}. Você {resultado["perdeu"]}.')
elif bot == 1:
    if player == 0:
        print(f'Você jogou {choices[player]} \
e o computador jogou {choices[bot]}. Você {resultado["perdeu"]}.')
    else:
        print(f'Você jogou {choices[player]} \
e o computador jogou {choices[bot]}. Você {resultado["ganhou"]}.')
else:
    if player == 0:
        print(f'Você jogou {choices[player]} \
e o computador jogou {choices[bot]}. Você {resultado["ganhou"]}.')
    else:
        print(f'Você jogou {choices[player]} \
e o computador jogou {choices[bot]}. Você {resultado["perdeu"]}.')
print('-=' * 40)
