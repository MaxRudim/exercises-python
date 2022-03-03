print('-=' * 40)

print('Boletim com listas compostas.')

print('-=' * 40)

students = list()

student = list()

while True:
    student.append(str(input('Digite o nome do estudante: ')))

    student.append([float(input('Digite \
a primeira nota do estudante: '))])

    student[1].append(float(input('Digite a segunda nota do estudante: ')))

    students.append(student[:])

    student.clear()

    go_on = str(input('Voce deseja continuar? [S/N] ')).strip().upper()[0]

    if go_on in 'Nn' or go_on not in 'Ss':
        break

print('')

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')

for num in range(len(students)):

    print('-' * 30)

    print(f'{num:<4}{students[num][0].capitalize():<10}\
{sum(students[num][1]) / len(students[num][1]):>8}')

print('-' * 30)

print('')

while True:
    n = int(input('Deseja mostrar as notas de qual aluno? '))

    print(f'As notas de {students[n][0].capitalize()} foram: {students[n][1]}')

    go_on = str(input('Deseja mostrar verificar \
mais alunos? [S/N]: ')).upper().strip()[0]

    if go_on in 'Nn' or go_on not in 'Ss':
        break

print('Finalizando...')

print('<<< VOLTE SEMPRE! >>>')
