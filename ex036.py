preço = int(input('Digite o valor da casa que pretende adquirir: R$ '))
salario = int(input('Digite o seu salário: R$ '))
anos = int(input('Digite em até quantos anos pretende pagar a casa: R$ '))

parcelas = anos * 12
mensalidade = preço / parcelas
limite = salario + (salario * 30 / 100)

if mensalidade > limite:
    print('Financiamento negado! O valor da mensalidade \
excede o limite salarial')
else:
    print('Financiamento concedido, boa sorte!')
