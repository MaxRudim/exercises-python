print('-=' * 40)

print(f'{"Simulador de caixa eletrônico.":^30}')
# Obs. O banco te cédulas de 50, 20, 10 e 1 real.

print('-=' * 40)

value = int(input('Qual valor voce quer sacar? R$ '))
total = value

ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced:.2f}.')

        if ced == 50:
            ced = 20

        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 1

        totced = 0

        if total == 0:
            break

print('\n')
print('=' * 50)

print('Operação efetuada com sucesso. Volte sempre!')

print('=' * 50)
