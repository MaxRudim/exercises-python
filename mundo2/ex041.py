from datetime import date

current_year = date.today().year

competitor_birth_year = int(input('Digite seu ano de nascimento: '))

age = current_year - competitor_birth_year

if age <= 9:
    print(f'Você possui {age} anos e compete na categoria MIRIM!')
elif age <= 14:
    print(f'Você possui {age} anos e compete na categoria INFANTIL!')
elif age <= 19:
    print(f'Você possui {age} anos e compete na categoria JUNIOR!')
elif age <= 20:
    print(f'Você possui {age} anos e compete na categoria SENIOR!')
else:
    print(f'Você possui {age} anos e compete na categoria MASTER!')
