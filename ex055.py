print('Mostra o maior e o menor peso')

weights = list()

for element in range(1, 6):
    weight = float(input('Digite um peso, em números, separado por ponto: '))
    weights.append(weight)

print(f'Peso máximo: {max(weights)}, peso mínimo: {min(weights)}')
