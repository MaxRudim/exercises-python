def leiaInt(inpt):
    num = str(input(inpt))

    while num.isnumeric() is False:
        print('ERRO! Digite um número inteiro válido!')
        num = str(input(inpt))

    return int(num)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
