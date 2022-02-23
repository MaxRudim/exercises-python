c = input('Em qual cidade voce nasceu? ').lower().strip()

city = c.split()

nasceu_cidade = 'santo' in city[0]

print(nasceu_cidade)
