data = input('Digite qualquer coisa: ')

print(f'Qual o tipo primitivo do resultado? {type(data)}')
print(f'Só tem espaços? {data.isspace()}')
print(f'O resultado é um número? {data.isnumeric()}')
print(f'O resultado é uma palavra? {data.isalpha()}')
print(f'O resultado é uma palavra OU um número? {data.isalnum()}')
print(f'O resultado está em letra maíscula? {data.isupper()}')
print(f'O resultado está em letra minúscula? {data.islower()}')
print(f'O resultado está capitalizada? {data.istitle()}')
