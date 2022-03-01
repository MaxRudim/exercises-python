from datetime import date

print('Contador de maioridade.')

current_year = date.today().year
count_minors = 0
count_adults = 0
ages = list()

for num in range(1, 8):
    age = int(input('Digite um ano de nascimento: '))
    ages.append(age)

for age in ages:
    if int(current_year) - int(age) >= 18:
        count_adults += 1
    else:
        count_minors += 1

print(f'Existe um total de {count_minors} pessoas menores de idade \
e {count_adults} pessoas adultas.')
