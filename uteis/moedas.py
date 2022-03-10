def metade(p):
    return p / 2


def dobro(p):
    return p * 2


def aumentar(p, percent):
    return p + (p * percent / 100)


def diminuir(p, percent):
    return p - (p * percent / 100)


def moedas(p):
    p = f'R$ {p:.2f}'
    brl = p.replace('.', ',')
    return brl
