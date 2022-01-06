while True:
    n1 = float(input())
    n2 = float(input())
    media = (n1 + n2)/2
    if media == 10:
        print('Aprovado com Distinção')
    elif media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')
