nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = float((nota1 + nota2) / 2)

if media < 5.0:
    print(f'Sua média foi de: {media}. Você foi REPROVADO!')
elif media >= 5.0 and media < 7:
    print(f'Sua média foi de {media}. Você está em RECUPERAÇÃO!')
else:
    print(f'Sua média foi de {media}. Você foi APROVADO!')
