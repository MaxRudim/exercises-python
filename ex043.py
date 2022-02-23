height = float(input('Digite sua altura, em metros: '))
weight = float(input('Digite seu peso, em kgs: '))

imc = float(weight / (height ** 2))

if imc < 18.5:
    print(f'Você possui um IMC de: {round(imc, 2)}, \
equadrando-se na categoria: ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print(f'Você possui um IMC de: {round(imc, 2)}, \
equadrando-se na categoria: PESO IDEAL!')
elif 25 <= imc < 30:
    print(f'Você possui um IMC de: {round(imc, 2)}, \
equadrando-se na categoria: SOBREPESO!')
elif 30 <= imc < 40:
    print(f'Você possui um IMC de: {round(imc, 2)}, \
equadrando-se na categoria: OBESIDADE!')
else:
    print(f'Você possui um IMC de: {round(imc, 2)}, \
equadrando-se na categoria: OBESIDADE MÓRBIDA!')
