sum = 0

for num in range(1, 501):
    if num % 2 != 0 and num % 3 == 0:
        sum += num
print(sum)
