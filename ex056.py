ages = list()
males = dict()
less_than_21_yo_female_count = 0

for p in range(1, 5):
    print(f'---- {p}ª PESSOA ----')
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    ages.append(age)
    gender = str(input('Gênero [M/F]: ')).strip().upper()
    if gender == 'M':
        males[name] = age
    else:
        if age < 20:
            less_than_21_yo_female_count += 1

average_ages = sum(ages) / len(ages)

print(f'A média de idade do grupo é: {average_ages} anos.')

print(f'O homem mais velho do grupo é: {max(males, key=males.get)}, \
com {max(males.values())} anos de idade.')

print(f'{less_than_21_yo_female_count} \
mulheres possuem menos de 20 anos de idade.')
