frase = 'Curso em Vídeo Python'
frase_list = ['C', 'u', 'r', 's', 'o', ' ', 'e', 'm',
              ' ', 'V', 'í', 'd', 'e', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n']

# -- Fatiamento -- #
# Obs. TAMBÉM É APLICÁVEL ÀS TUPLAS.

frase[9]  # Retorno:'V'

frase[9:13]  # Retorno: 'Víde'

frase[9:21]  # Retorno: 'Vídeo Python'
#  Obs acima: a frase tem apenas 20 caracteres,
#  mas conta-se apenas o primeiro, excluindo o ultimo
#  Então o 21, como seria excluido, faria com que apenas o 'n' fosse pego.

frase[9:21:2]  # Retorno: 'VdoPto'
#  Obs acima: pega o elemento de índice 9 até o 21
#  (frase tem 21 caracteres, o ultimo não conta)
#  e pula de 2 em 2. Se colocar -1 no final,
#  roda a frase em ordem decrescente, ex frase[::-1]

frase[:5]  # Retorno: 'Curso'
#  Obs acima: quando não há elementos antes do ':',
#  considera-se como se fosse o primeiro

frase[15:]  # Retorno: 'Python'
#  Obs acima: vai do elemento 15 até o fim da frase

frase[9::3]  # Retorno: 'VePh'
#  Obs acima: roda do elemento 9 até o fim da frase, pulando de 3 em 3

# -- Análise -- #

len(frase)  # Retorno: 21
#  Obs acima: a frase tem 21 caracteres, com índices de 0 a 20

frase.count('o')  # Retorno: 3
#  Obs acima: case sensitive

frase.count('o', 0, 13)  # Retorno: 1
#  Obs acima: conta as letras 'o' do índice 0 até o
#  índice 12 (o índice 13, correspondente à outra letra 'o', não é incluso)

frase.find('deo')  # Retorno: 11
#  Obs acima: retorna o índice em que a palavra buscada começou a aparecer

frase.find('Android')  # Retorno: -1

'Curso' in frase  # Retorno: True

# -- Transformação -- #

frase.replace('Python', 'Android')  # Retorno: 'Curso em Vídeo Android'
#  Obs acima: não substitui diretamente na string, mas de forma secundária

frase.upper()  # Retorno: 'CURSO EM VÍDEO PYTHON'

frase.lower()  # Retorno: 'curso em vídeo python'

frase.capitalize()  # Retorno: 'Curso em vídeo python'

frase.title()  # Retorno: 'Curso Em Vídeo Python'

nova_frase = '   Aprenda Python  '
nova_frase_list = [' ', ' ', ' ', 'A', 'p', 'r', 'e', 'n', 'd', 'a', ' ',
                   'P', 'y', 't', 'h', 'o', 'n', ' ', ' ']

nova_frase.strip()  # Retorno: 'Aprenda Python'
# Obs acima: remove todos os espaços do início e do fim da frase

nova_frase.rstrip()  # Retorno: '   Aprenda Python'
# Obs acima: remove todos os espaços do fim da frase

nova_frase.lstrip()  # Retorno: 'Aprenda Python  '
# Obs acima: remove todos os espaços do começo da frase

# -- Divisão -- #

frase.split()
# Retorno: ['Curso', 'em', 'Vídeo, 'Pyhon']
# Obs acima: pode ir acessando os elementos,
# ex: dividido = frase.split()
# dividido[0] == 'Curso'
# dividido[0][0] == 'C'

# -- Junção -- #

'-'.join(frase)  # Retorno: Curso-em-Vídeo-Python


# Obs: usar print(""""frase grande"""")
# para escrever frase grande de forma fácil.
