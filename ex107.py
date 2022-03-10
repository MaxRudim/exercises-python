from uteis import moedas


p = float(input('Digite o preço: R$ '))

print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10% de {p}, temos {moedas.aumentar(p, 10)}')
print(f'Diminuindo 13% de {p}, temos {moedas.diminuir(p, 13)}')
