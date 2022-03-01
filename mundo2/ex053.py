print('-=' * 30)

print('Verificador de palíndromos.')

print('-=' * 30)

phrase = str(input('Digite uma palavra ou frase: ')).strip().lower()

s_phrase = phrase.split()
j_phrase = ''.join(s_phrase)
rev = ''

# j_phrase -1 é a última letra da frase,
# o segundo -1 é para a contagem ir até o índice 0
# e o terceiro -1 é para ser contagem decrescente em 1
for word in range(len(j_phrase) - 1, -1, -1):
    rev += j_phrase[word]

if rev == j_phrase:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
