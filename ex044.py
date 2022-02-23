print('===== SUPER MAX ATACADISTA =====')
price = float(input('Digite o preço das compras: R$ '))

print('Opções de pagamento: ')
print('''
[1] à vista: dinheiro/cheque
[2] à vista: cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')

option = int(input('Digite o número de sua opção: '))

if option == 1:
    preço = price - (price * 10 / 100)
    print(f'O valor total da compra é: R$ {round(preço, 2)}, \
com desconto de: R$ {round(price * 10 / 100)}, \
devendo ser paga em 1 parcela.')
elif option == 2:
    preço = price - (price * 5 / 100)
    print(f'O valor total da compra é: R$ {round(preço, 2)}, \
com desconto de: R$ {round(price * 5 / 100)}, \
devendo ser paga em 1 parcela.')
elif option == 3:
    print(f'O valor total da compra será: R$ {round(price, 2)}. \
Devendo ser paga em duas parcelas de: R$ {round((price / 2), 2)}')
elif option == 4:
    parcelas = int(input('Em quantas parcelas pretende pagar? '))
    if parcelas < 3:
        print('Caso queira pagar em menos de 3 parcelas, \
utilize as opções 1, 2 ou 3.')
    else:
        preço = price + (price * 20 / 100)
        print(f'O valor total da compra será: R$ {round(preço, 2)}, \
os juros foram de: R$ {round((price * 20 / 100), 2)}. \
O valor total deve ser pago em {parcelas} \
parcelas de: R$ {round((preço / parcelas), 2)}')
else:
    print('Opção inválida. \
Digite outra opção de pagamento conforme indicado acima.')
