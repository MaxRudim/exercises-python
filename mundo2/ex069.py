print('-=' * 40)

print('Analisador de dados do grupo')

print('-=' * 40)

more_than_18 = males = female_less_than_20_yo = 0
sex_validation = 'HM'

while True:
    idade = int(input('Qual a idade do usuário(a)? '))
    sex = str(input('Qual o sexo do usuário(a) [H/M]? ')).strip().upper()[0]
    while sex not in sex_validation:
        sex = str(input('Digite apenas Homem ou Mulher \
para cadastrar o sexo do usuário: ')).strip().upper()[0]
    if idade > 18:
        more_than_18 += 1
    if sex == 'M':
        males += 1
    else:
        if idade < 20:
            female_less_than_20_yo += 1

    keep_running = str(input('\nDeseja continuar \
a execução do programa? [S/N]')).strip().upper()[0]

    if keep_running == 'N':
        break

print('\n-=' * 40)
print('Programa encerrado!')
print('-=' * 40)

print(f'\nForam cadastrados um total de {more_than_18} \
pessoas com mais de 18 anos.')

print(f'\nForam cadastrados um total de {males} \
pessoas do sexo masculino.')

print(f'\nForam cadastrados um total de {female_less_than_20_yo} \
mulheres com menos de 20 anos de idade.')
