print('-=' * 40)

print('Lista composta e análise de dados.')

print('-=' * 40)

person = list()
group = list()
mai = men = 0

while True:
    person.append(str(input('Digite o nome da pessoa para o cadastro: ')))
    person.append(float(input('Digite o peso da pessoa acima: ')))
    if len(group) == 0:
        mai = men = person[1]
    else:
        if person[1] > mai:
            mai = person[1]
        if person[1] < men:
            men = person[1]

    group.append(person[:])
    person.clear()
    go_on = str(input('Voce deseja continuar? [S/N] ')).strip().upper()
    if go_on in 'Nn':
        break

print('-' * 40)
print(f'As pessas cadastradas foram: {group}')
print('')
print(f'Quantidade de pessoas cadastradas: {len(group)}')
print('')
print(f'O maior peso foi de: {mai}, pertencente à: ', end='')
for p in group:
    if p[1] == mai:
        print(f'[{p[0]}]')
print('')
print(f'O menor peso foi de: {men}, pertencente à: ', end='')
for p in group:
    if p[1] == men:
        print(f'[{p[0]}]')
