sum = 0

for num in range(1, 501):
    if num % 2 != 0 and num % 3 == 0:
        sum += num

# maneira mais simples de fazer, com menos iterações
# for num in range(1, 501, 2):
#     if num % 3 == 0:
#         sum += num


print(sum)
