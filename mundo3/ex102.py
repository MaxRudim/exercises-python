from math import factorial


def fatorial(num, show=False):
    """
    -> Função para o cálculo de fatoriais.
    :param num: numero que terá seu fatorial calculado

    :param show: (opcional) booleano para mostrar ou não
    - o processo de cálculo do fatorial

    :return: retorna um print do processo de elaboração do fatorial caso show
    - seja True ou apenas o print do resultado do
    - fatorial caso o show seja falso ou não seja passado.

    Obs: Aperte a tecla Q para sair do modo help.
    """
    if show is True:
        c = num
        f = 1
        while c > 0:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
            f = f * c
            c -= 1
        print(f'{f}')

    else:
        print(f'O fatorial de {num} é {factorial(num)}')


help(fatorial)
