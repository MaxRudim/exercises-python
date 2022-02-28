print('-=' * 40)

print('Contador de números')

print('-=' * 40)


count = s = 0

while True:
    n = int(input('Digite um número [999 para encerrar]: '))
    if n == 999:
        break
    count += 1
    s += n

print(f'Você digitou {count} números')
print(f'A soma dos números que voce digitou é: {s}')
