salario = float(input("Qual o seu salário? "))

if (salario > 2000):
    percentual = 7
else:
    percentual = 15

percentual = percentual/100
aumento = percentual * salario
novo_salario = salario + aumento

print("Novo salário: R$ ", novo_salario)