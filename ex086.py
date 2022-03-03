print('-=' * 40)

print('Matriz em python')

print('-=' * 40)

row1 = list()
row2 = list()
row3 = list()


for n in range(0, 3):
    num = int(input(f'Digite um valor para [0, {n}]: '))
    row1.append([num])

for n in range(0, 3):
    num = int(input(f'Digite um valor para [1, {n}]: '))
    row2.append([num])

for n in range(0, 3):
    num = int(input(f'Digite um valor para [0, {n}]: '))
    row3.append([num])

print('-' * 80)
print('')
print('Sua matriz aqui: ')
print('')
print(row1[0], row1[1], row1[2])
print(row2[0], row2[1], row2[2])
print(row3[0], row3[1], row3[2])
