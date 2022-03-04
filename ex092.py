from datetime import date

worker = dict()

this_year = date.today().year

worker['Nome'] = str(input('Digite seu nome: '))

nasc_data = int(input('Digite o ano de seu nascimento: '))

worker['Idade'] = this_year - nasc_data

worker['Carteira de Trabalho'] = int(input('Digite sua cartera de trabalho \
([0] = não tem): '))

if worker['Carteira de Trabalho'] > 0:

    worker['Ano de Contratação'] = int(input('Digite o ano  \
da sua contratação: '))

    retirement = worker['Idade'] + \
        (worker['Ano de Contratação'] + 35) - this_year

    worker['Salário'] = int(input('Digite seu salário: '))

    worker['Aposentadoria'] = retirement

    for k, v in worker.items():
        print(f'{k.lower()} tem o valor {v}')

elif worker['Carteira de Trabalho'] == 0:

    for k, v in worker.items():
        print(f'{k.lower()} tem o valor {v}')

else:
    print('Os dados da Carteira de Trabalho estão incorretos.')
