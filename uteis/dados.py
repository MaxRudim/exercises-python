def leiaDinheiro(inpt):
    valido = False

    while not valido:
        entry = str(input(inpt)).replace(',', '.').strip()

        if entry.isalpha() or entry == '':
            print(f'\033[0;31mERRO: "{entry}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entry)
