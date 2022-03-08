def area(lar, c):
    print('')
    print('-' * 40)
    print(f'A área de um terreno {lar} x {c} é de: {lar * c}m².')
    print('-' * 40)


print('Controle de Terrenos')
print('-' * 40)

lar = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))

area(lar, c)
