from ast import Interactive


def somar(a, b):
    c = a + b
    return c

a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))
x = somar(a, b)
print(x)