def moedas(p):
    p = f'R$ {p:.2f}'
    brl = p.replace('.', ',')
    return brl


def metade(p, f=False):
    if f is True:
        return moedas(p / 2)
    else:
        return p / 2


def dobro(p, f=False):
    if f is True:
        return moedas(p * 2)
    else:
        return p * 2


def aumentar(p, percent, f=False):
    if f is True:
        return moedas(p + (p * percent / 100))
    else:
        return p + (p * percent / 100)


def diminuir(p, percent, f=False):
    if f is True:
        return moedas(p - (p * percent / 100))
    else:
        return p - (p * percent / 100)


def resumo(p, aumento=0, diminuição=0):
    print('-' * 50)
    print('RESUMO DO VALOR')
    print('-' * 50)

    print(f'Preço analisado: {moedas(p)}')

    print(f'A metade de {moedas(p)} é {metade(p, True)}')

    print(f'O dobro de {moedas(p)} é {dobro(p, True)}')

    print(f'Aumentando {aumento}% de {moedas(p)}, \
temos {aumentar(p, aumento, True)}')

    print(f'Diminuindo {diminuição}% de {moedas(p)}, \
temos {diminuir(p, diminuição, True)}')

    print('-' * 50)
