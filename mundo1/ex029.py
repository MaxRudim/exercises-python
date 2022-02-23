from random import randint

vel = randint(10, 200)

print(f'Voce trafegou na velocidade de: {vel} km/h')

if vel > 80:
    multa = float((vel - 80) * 7)
    print(f'Como sua velocidade excedeu em {vel - 80} \
o limite da pista, voce foi multado em: R$ {round(multa, 3)}')

print('Dirija com prudência!')
