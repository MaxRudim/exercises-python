print('-=' * 40)

print('Somador de números inteiros python.')

print('-=' * 40)

num = c = s = 0
num = int(input('Digite um número inteiro: [999 para parar] '))
while num != 999:
    s += num
    c += 1
    num = int(input('Digite um número inteiro: [999 para parar] '))

print(f'Você digitou {c} números. A soma entre eles é: {s}')
