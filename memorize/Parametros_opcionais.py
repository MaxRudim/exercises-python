# quando iguala o parametro à zero ele se torna facultativo.
def somar(a=0, b=0, c=0):
    global oi
    oi = 9
    s = a + b + c
    print(f'A soma vale {s}')


oi = 2
somar(c=1, b=2)  # Obs é possível determinar qual parametro voce quer definir.
print(oi)  # oi se tornou 9 pois, embora a função tenha escopo específico,
#  quando utiliza-se o global o escopo da variável torna-se global,
# alterando o oi fora da função.
