from uteis import moedas


p = float(input('Digite o preço: R$ '))

print(f'A metade de {moedas.moedas(p)} é {moedas.metade(p, True)}')

print(f'O dobro de {moedas.moedas(p)} é {moedas.dobro(p, True)}')

print(f'Aumentando 10% de {moedas.moedas(p)}, \
temos {moedas.aumentar(p, 10, True)}')

print(f'Diminuindo 13% de {moedas.moedas(p)}, \
temos {moedas.diminuir(p, 13, True)}')
