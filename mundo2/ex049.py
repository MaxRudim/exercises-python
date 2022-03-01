number = int(input('Digite um número para saber sua tabuada: '))

for num in range(10, -1, -1):
    print(f'{number} x {num} = {number * num}')
print('FIM!')
