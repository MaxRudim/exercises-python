def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno

    Esta string adiciona informações quando usa-se o help(contador),
    facilitando entender a funcionalidade.

    Obs: Aperte Q para fechar o help(contador)
    """
    c = i

    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)
