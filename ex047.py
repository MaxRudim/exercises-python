pares = list()

for n in range(0, 51):
    if n % 2 == 0:
        pares.append(n)
print(', '.join([str(elem) for elem in pares]))
