from random import randint
from math import trunc, sqrt, hypot

cateto_oposto = randint(6, 16)
cateto_adjacente = randint(1, 10)

print(f'O cateto oposto é de: {cateto_oposto}m, \
o cateto adjacente é de: {cateto_adjacente}m \
. Logo, a hipotenusa é de: \
{trunc(sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)))}')

# OUTRAS RESOLUÇÕES
print(f'O cateto oposto é de: {cateto_oposto}m, \
o cateto adjacente é de: {cateto_adjacente}m \
. Logo, a hipotenusa é de: \
{round((cateto_adjacente ** 2 + cateto_oposto ** 2) ** (1 / 2), 2)}')

# ----------------------------------------
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O cateto oposto é de: {cateto_oposto}m, \
o cateto adjacente é de: {cateto_adjacente}m \
. Logo, a hipotenusa é de: \
{round(hipotenusa, 2)}')
