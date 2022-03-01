print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)

tupla = ('Pão', 1.00,
         'Mortadela', 3.50,
         'Queijo', 2.20,
         'Goiabada', 5.00,
         'Picanha', 300.50,
         'Óleo', 15.00,
         'Sal kg', 7.00,
         'Tomate', 9.00,
         'Milho', 10.00)

for index in range(0, len(tupla)):
    if index % 2 == 0:
        print(f'{tupla[index]:.<30}', end='')
    else:
        print(f'R$ {tupla[index]:>5.2f}')
print('-' * 40)
