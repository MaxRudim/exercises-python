from datetime import date


def voto(nasc_ano):
    cur_year = date.today().year
    age = cur_year - nasc_ano

    if 18 < age < 70:
        return 'OBRIGATÓRIO!'
    elif 16 <= age < 18 or age > 70:
        return 'FACULTIVATIVO!'
    else:
        return 'NEGADO!'


nasc = int(input('Digite o ano de seu nascimento: '))

print(f'Seu voto é {voto(nasc)}')
