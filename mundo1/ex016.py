import random
from math import floor, trunc

random_number = random.random() * 10

print(f'O número aleatório foi: {random_number}, \
arredondado para baixo fica: {floor(random_number)}')

# OUTRAS RESOLUÇÕES:
print(f'O número aleatório foi: {random_number}, \
arredondado para baixo fica: {trunc(random_number)}')

# ---------------
print(f'O número aleatório foi: {random_number}, \
arredondado para baixo fica: {int(random_number)}')
