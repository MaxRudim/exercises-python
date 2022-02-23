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
    print('Sua idade excedeu a idade de alistamento militar!')
