n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro número é maior que o segundo')
elif n2 > n1:
    print('O segundo número é maior que o primeiro')
else:
    print('Não existem números maiores, ambos possuem o mesmo valor')
