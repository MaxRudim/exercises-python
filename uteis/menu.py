def leiaInt(inpt):

    while True:
        try:
            num = int(input(inpt))

        except (ValueError, TypeError):

            print('\033[31mERRO: digite um número inteiro válido.\033[m')
            continue  # Obs: o continue joga o laço para o começo de novo.

        except KeyboardInterrupt:

            print(' \033[31mO usuário decidiu \
interromper a operação!\033[m')
            return 3

        else:
            return num


def linha(tam=42):
    return '-' * 42


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    option = leiaInt('\033[32mSua Opção: \033[m')
    return option
