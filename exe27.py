#Leia dois números, calcule e informe a soma. Pergunte se deseja calcular novamente.

verificador = "s"

while verificador == "s" or verificador == "S":
    primeiroValor = int(input("Informe o 1° valor: "))
    segundoValor = int(input("Informe o 2° valor: "))
    soma = primeiroValor + segundoValor
    print(f"A soma dos números {primeiroValor} e {segundoValor} é de: {soma}")
    verificador = input("Quer continuar? (S / N ): ")
else:
    print("Fim do enlace")