num = int(input('Digite um número: '))

mil = num // 1000 % 10
cen = num // 100 % 10
dez = num // 10 % 10
uni = num // 1 % 10

print(f'Analisando o número: {num}')

print(mil)

print(f"""unidade: {uni}, \
dezena: {dez}, \
centena: {cen}, \
milhar: {mil}.""")
