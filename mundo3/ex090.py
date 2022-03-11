estudante = dict()

estudante['Nome'] = str(input('Nome: '))
estudante['Média'] = float(input(f'Média de {estudante["Nome"]}: '))
if estudante['Média'] >= 6.0:
    estudante['Situação'] = 'Aprovado(a)'
else:
    estudante['Situação'] = 'Reprovado(a)'

for k, v in estudante.items():
    print(f'{k} é igual a {v}')
