lol = "vasya;12,lexa;16,petya;64"

list = [x.split(';') for x in lol.split(',')]
sorted_list = sorted(list, key=lambda x: int(x[1]))
old_filter = [x for x in sorted_list if int(x[1]) < 50]


print(old_filter)

