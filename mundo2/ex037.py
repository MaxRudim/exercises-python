number = int(input('Digite um número intero: '))
print('Escolha uma das seguintes bases para a conversão:')
print('''
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL
''')
option = int(input('Digite o número de sua opção: '))

if option not in [1, 2, 3]:
    print('Digite uma opção válida!')
elif option == 1:
    print(f'{number} convertido para binário é: {bin(number)}')
elif option == 2:
    print(f'{number} convertido para octal é: {oct(number)}')
else:
    print(f'{number} convertido para hexadecimal é: {hex(number)}')
