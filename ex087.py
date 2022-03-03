print('-=' * 40)

print('Mais sobre matriz em python')

print('-=' * 40)

# Obs. Diferente do exercício anterior, esta matriz foi feita conforme a aula
spar = mai = scol = 0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for li in range(0, 3):
    for co in range(0, 3):
        matriz[li][co] = int(input(f'Digite um valor para [{li}, {co}]: '))

print('-=' * 40)
for li in range(0, 3):
    for co in range(0, 3):
        print(f'[{matriz[li][co]:^5}]', end='')
        if matriz[li][co] % 2 == 0:
            spar += matriz[li][co]

    print()
print('-=' * 40)
print(f'A soma dos números pares da matriz é: {spar}')
for li in range(0, 3):
    scol += matriz[li][2]
print(f'A soma dos valores da terceira coluna é: {scol}')
for co in range(0, 3):
    if co == 0:
        mai = matriz[1][co]
    else:
        if matriz[1][co] > mai:
            mai = matriz[1][co]
print(f'O maior valor na segunda linha da matriz é: {mai}')
