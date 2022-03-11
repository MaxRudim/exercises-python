def leiaInt(inpt):

    while True:
        try:
            num = int(input(inpt))

        except (ValueError, TypeError):

            print('\033[31mERRO: digite um número inteiro válido.\033[m')
            continue  # Obs: o continue joga o laço para o começo de novo.

        except KeyboardInterrupt:

            print(' -> \033[31mERRO: O usuário decidiu \
interromper a operação!\033[m')
            break

        else:
            return num


n = leiaInt('Digite um número: ')

if n is not None:
    print(f'Você acabou de digitar o número {n}')
