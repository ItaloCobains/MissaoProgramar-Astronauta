str = 'The quick brown fox'
str_reservada = []
i = len(str)
while i > 0:
    str_reservada += str[i-1]
    i = i - 1

StrA = "".join(str_reservada)

print(f'{str}, {StrA}')
