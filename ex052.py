
number = int(input('Digite um número para verificar se ele é primo: '))

count = 0

for num in range(1, number + 1):
    if number % num == 0:
        count += 1

if count == 2:
    print(f'O número {number} é primo.')
else:
    print(f'O número {number} não é primo.')
