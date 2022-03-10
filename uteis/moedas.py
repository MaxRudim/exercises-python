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
