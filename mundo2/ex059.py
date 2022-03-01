print('-=' * 40)

print('Atendente de operação de números.')

print('-=' * 40)

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

operation = 0

print('Opções de operações: ')
print('''
[1] Soma entre os dois números digitados
[2] Multiplicação entre os dois números digitados
[3] Verificação do maior número digitado
[4] Digite novos números
[5] Sair do programa
''')

while operation != 5:
    operation = int(input('\nQual a operação desejada? '))

    if operation == 1:
        print(f'A soma de {n1} com {n2} é: {n1 + n2}')
    elif operation == 2:
        print(f'O produto de {n1} com {n2} é: {n1 * n2}')
    elif operation == 3:
        higher = list([n1, n2])
        print(f'O maior número digitado é: {max(higher)}')
    elif operation == 4:
        print('\nDigite novos números abaixo.')
        n1 = int(input('\nPrimeiro número: '))
        n2 = int(input('Segundo número: '))
    elif operation not in [1, 2, 3, 4, 5]:
        print('Número de operação inválido. Encerrando o programa.')
        operation = 5

print('Programa encerrado com sucesso. Tenha um bom dia.')
