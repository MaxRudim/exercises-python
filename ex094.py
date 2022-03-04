dados = list()
pessoa = dict()
women = list()
s_age = 0

while True:
    pessoa['Nome'] = str(input('Nome: ')).strip().capitalize()

    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if pessoa['Sexo'] in 'Ff':
        women.append(pessoa['Nome'])

    pessoa['Idade'] = int(input('Idade: '))

    s_age += pessoa['Idade']

    dados.append(pessoa.copy())

    go_on = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if go_on in 'Nn' or go_on not in 'Ss':
        break

print('-=' * 30)

print(f'O grupo tem {len(dados)} pessoas.')

avg_age = s_age / len(dados)

print(f'A média de idade é de: {avg_age} anos.')

print(f'As mulheres cadastradas foram: {", ".join(women)}')

print('Lista de pessoas que estão acima da idade média: ')

print('')

for element in dados:
    if element['Idade'] > avg_age:
        print(f'Nome = {element["Nome"]}, Sexo = {element["Sexo"]}, \
Idade = {element["Idade"]}')

        print('')

print('<< ENCERRADO! >>')
