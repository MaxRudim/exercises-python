def notas(*num, sit=False):
    """
    -> Função que apresenta dados sobre o desempenho de um aluno.

    :param num: recebe qualquer quantidade de notas enviadas por parâmetro

    :param sit: (opcional) Booleano que, se for True (sit=True),
        -> mostra comentário sobre a situação do aluno, com base em sua média

    Pressione Q para sair do modo help(notas).
    """
    result = dict()
    result['Total'] = len(num)
    result['Maior'] = max(num)
    result['Menor'] = min(num)
    result['Média'] = round(sum(num) / len(num), 1)

    if sit is True:
        if result['Média'] >= 8.0:
            result['Situação'] = 'Boa'
        elif result['Média'] > 6.0:
            result['Situação'] = 'Razoável'
        else:
            result['Situação'] = 'Ruim'

    return result


resp = notas(3.5, 4, 5.2, 8.6, sit=True)

print(resp)
