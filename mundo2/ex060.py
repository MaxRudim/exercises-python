print('-=' * 40)

print('Calculadora de fatoriais.')

print('-=' * 40)

n = int(input('Digite um número positivo inteiro para saber seu fatorial: '))

c = n

f = 1

print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f'{f}')
