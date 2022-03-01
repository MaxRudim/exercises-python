print('-=' * 50)

print('Analisador de números em tuplas')

print('-=' * 50)

n1 = int(input('Digite um número inteiro e positivo qualquer: '))
n2 = int(input('Digite outro número inteiro e positivo qualquer: '))
n3 = int(input('Digite outro número inteiro e positivo qualquer: '))
n4 = int(input('Digite outro número inteiro e positivo qualquer: '))

lista = list([n1, n2, n3, n4])
tupla = tuple(lista)

par = 0
for n in tupla:
    if n % 2 == 0:
        par += 1

print(f'Você digitou os valores: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O primeiro valor 3 foi apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Foram digitados um total de {par} números pares.')
