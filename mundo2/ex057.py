print('-=' * 40)

print('Verificador de sexo usando while.')

print('-=' * 40)

sex = input('Digite seu sexo [M / F]: ').strip().upper()[0]

while sex not in 'MF':
    sex = input('Dados inválidos, \
por favor informe seu sexo [M / F]: ').strip().upper()[0]

print(f'Sexo {sex} registrado com sucesso.')
