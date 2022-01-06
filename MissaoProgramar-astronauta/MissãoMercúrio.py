"""
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

"""

salario = float(input())

if salario <= 280.00:
    percentual = 20
    salarioa = (salario * percentual / 100)
    salarion = salario + salarioa
    print(f"""
            o salário antes do reajuste = {salario}
            o percentual de aumento aplicado = {percentual}%
            o valor do aumento = {salarioa}
            o novo salário, após o aumento = {salarion}
    """)
elif salario > 280.00 and salario <= 700.00:
    percentual = 15
    salarioa = (salario * percentual / 100)
    salarion = salario + salarioa
    print(f"""
            o salário antes do reajuste = {salario}
            o percentual de aumento aplicado = {percentual}%
            o valor do aumento = {salarioa}
            o novo salário, após o aumento = {salarion}
    """)
elif salario > 700.00 and salario <= 1500.00:
    percentual = 10
    salarioa = (salario * percentual / 100)
    salarion = salario + salarioa
    print(f"""
            o salário antes do reajuste = {salario}
            o percentual de aumento aplicado = {percentual}%
            o valor do aumento = {salarioa}
            o novo salário, após o aumento = {salarion}
    """)
elif salario > 1500.00:
    percentual = 5
    salarioa = (salario * percentual / 100)
    salarion = salario + salarioa
    print(f"""
            o salário antes do reajuste = {salario}
            o percentual de aumento aplicado = {percentual}%
            o valor do aumento = {salarioa}
            o novo salário, após o aumento = {salarion}
    """)
else:
    print('ERRO')