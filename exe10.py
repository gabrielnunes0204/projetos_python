#Leia as medidas(b, h) de um retângulo. Informe a área calculada e se é um quadrado ou não.

base = float(input("Informe a base do retângulo: "))
altura = float(input("Informe a altura do retângulo: "))
areaRetangulo = base * altura

if base == altura:
    print(f"A área do retângulo é de {areaRetangulo}, e ele é um QUADRADO")
else:
    print(f"A área do retângulo é de {areaRetangulo}, e ele não é um QUADRADO")