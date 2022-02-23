nome = str(input('Digite o seu nome: ')).strip()

espaços = nome.count(' ')
primeiro_nome = nome.find(' ')

print('Analisando seu nome...')
print(f'Seu nome em maiúsculo é: {nome.upper()}')
print(f'Seu nome em minúsculo é: {nome.lower()}')
print(f'Sem espaços, seu nome possui: \
{len(nome)-espaços}')
print(f'Seu primeiro nome possui: \
{primeiro_nome}')

# Outra solução para o ultimo caso é: len(nome.split()[0])
