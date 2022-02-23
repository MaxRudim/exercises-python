fr = input('Digite uma frase: ').strip().lower()

count_a = fr.count('a')
find_a = fr.find('a')
find_last_a = fr.rfind('a')

print(f'Sua frase possui {count_a} letras "a"')
print(f'A primeira letra "a" aparece na posição: {int(find_a) + 1}')
print(f'A última letra "a" aparece na posição: {int(find_last_a) + 1}')
