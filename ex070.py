print('-=' * 40)

print('Analisador de produtos do supermercado')

print('-=' * 40)

totalspent = how_many_costs_more_than_1000 = 0
products = dict()

while True:
    product_name = str(input('\nQual o nome \
do produto? ')).strip().capitalize()

    preço = float(input('Qual o preço do produto? '))

    if preço > 0:
        totalspent += preço
    else:
        preço = float(input('Digite um preço maior que 0, \
com as casas decimais separadas por ".": R$ '))

    if preço > 1000:
        how_many_costs_more_than_1000 += 1

    products[f"{product_name}"] = preço

    keep_running = str(input('\nDeseja continuar \
a execução do programa? [S/N]')).strip().upper()[0]

    if keep_running == 'N':
        break

print('\n-=' * 40)
print('Programa encerrado!')
print('-=' * 40)

print(f'\nO valor total gasto na compra é de: R$ {totalspent:.2f}')

print(f'\n{how_many_costs_more_than_1000} produtos custam mais de R$ 1000.00.')

print(f'\nO produto mais barato foi: {min(products, key=products.get)}, \
custando: R$ {min(products.values()):.2f}.')
