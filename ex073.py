ranking = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí',
           'Botafogo', 'Ceará SC', 'Corinthians', 'Coritiba', 'Cuiabá',
           'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional',
           'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo')

# Acessando a tupla:
# print(ranking)

# Acessando os 5 primeiros colocados do ranking do brasileirão:
# print(ranking[:5])

# Acessando os últimos 4 colocados do ranking do brasileirão:
# print(ranking[16:])

# ou:

# last_four = len(ranking) - 4
# print(ranking[last_four:])

# Acessando a lista dos times em ordem alfabética, não mais de colocação:
# print(sorted(ranking))

# Obs... OO DROGA, EU JÁ TINHA PEGO A TUPLA EM ORDEM ALFABÉTICA,
# NÃO PELA COLOCAÇÃO DOS TIMES..

# O exercício pedia para retornar em que posição estava o time chapecoense,
# mas como ele não se encontra
# na tabela, farei com o Coritiba:
# print(ranking.index('Coritiba'))
