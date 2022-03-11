words = ('programação', 'linguagem', 'aprender', 'digitar', 'mercado',
         'trabalho', 'futuro', 'dinheiro', 'jogos', 'livro', 'curso')

for word in words:
    print(f'\nNa palavra {word.upper()}, temos: ', end='',)

    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
print('\n')
