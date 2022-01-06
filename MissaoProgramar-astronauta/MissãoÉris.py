list = []

list.append(int(input("Telefonou para a vítima?")))
list.append(int(input("Esteve no local do crime?")))
list.append(int(input("Mora perto da vítima?")))
list.append(int(input("Devia para a vítima?")))
list.append(int(input("Já trabalhou com a vítima?")))

sr = 0

for i in list:
    sr += int(i)

if sr < 2:
    print('Inocente')
elif sr == 2:
    print('Suspeito')
elif 3 <= sr <= 4:
    print('Cúmplice')
elif sr == 5:
    print('Assassino')
