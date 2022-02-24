pares = list()

# for n in range(0, 51):
for n in range(2, 51, 2):
    if n % 2 == 0:
        pares.append(n)
print(', '.join([str(elem) for elem in pares]))
