from random import randint, choice

aluno_sorteado = randint(0, 3)

alunos = list(['Marcos', 'Lucas', 'Max', 'Geovana'])

print(f'Foi sorteado o(a) aluno(a) de número: {aluno_sorteado + 1} \
e ele(a) é: {alunos[aluno_sorteado]}')

# OUTRA RESOLUÇÃO

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]

print(f'O aluno escolhido foi: {choice(lista)}')
