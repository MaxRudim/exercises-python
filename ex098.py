from time import sleep

# Obs.: Sem o flush=True tem um buffer de tela
# (a função printa só quando está completa) e parece que deu erro.


def contador(i, f, p):

    if p < 0:
        p *= -1

    if p == 0:
        print('Impossível processar passo = 0, então passo será 1.')
        p = 1

    print('-=' * 30)
    print(f'Contagem de {i} até {f}, de {p} em {p}')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')

    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


print('-=' * 30)
print('FUNÇÃO DE CONTADOR!')
print('-=' * 30)


print('')

contador(1, 10, 1)

contador(10, 0, 2)

print('')

print('Agora é sua vez de personalizar a contagem!')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
