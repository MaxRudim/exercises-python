from random import randint
import math

number = randint(1, 360)
# number = 45
angulo = math.radians(number)

print(f'O ângulo foi de: {angulo}º, \
sendo seu seno: {round(math.sin(angulo), 2)}º, \
cosseno: {round(math.cos(angulo), 2)}º e \
tangente: {round(math.tan(angulo), 2)}º')
