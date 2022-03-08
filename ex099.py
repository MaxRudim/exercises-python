def maior(* values):
    print('-=' * 30)

    print('Analisando os valores passados...')

    for val in values:
        print(f'{val} ', end='')

    print(f'Foram informados {len(values)} valores ao todo.')

    print(f'O maior valor informado foi {max(values)}.')


maior(2, 4, 6, 9, 10)
maior(2, 30, 16, 29, 100)
maior(5, 2, 1, 34, 14)
maior(23, 400, 64, 96, 16)
maior(6)
