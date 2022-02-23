from datetime import date

current_year = date.today().year

born = int(input('Digite o ano em que voce nasceu: '))

age = (current_year - born)

print(age)

if age < 18:
    print('Ainda não chegou sua epoca de se alistar nos serviço militar!')
elif age == 18:
    print('Bem vindo, soldado!')
else:
    print(f'Sua idade excedeu, em {age - 18} a idade de alistamento militar!')
