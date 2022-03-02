print('-=' * 40)

print('Validando expressões matemáticas')

print('-=' * 40)

exp = str(input('Digite uma expressão matemática e \
verifique se o uso dos parênteses está correto: '))

pilha = list()

for element in exp:
    if element == "(":
        pilha.append(element)
    elif element == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(element)
            break

if len(pilha) == 0:
    print('Expressão matemática válida!')
else:
    print('Expressão matemática inválida!')
