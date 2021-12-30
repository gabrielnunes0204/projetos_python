# Solicite um número de 1 a 12 e informe o mês escolhido por extenso.

mes = int(input("Informe um mês do ano por número (1...12): "))

if mes == 1:
    print("JANEIRO")
elif mes == 2:
    print("FEVEREIRO")
elif mes == 3:
    print("MARÇO")
elif mes == 4:
    print("ABRIL")
elif mes == 5:
    print("MAIO")
elif mes == 6:
    print("JUNHO")
elif mes == 7:
    print("JULHO")
elif mes == 8:
    print("AGOSTO")
elif mes == 9:
    print("SETEMBRO")
elif mes == 10:
    print("OUTUBRO")
elif mes == 11:
    print("NOVEMBRO")
elif mes == 12:
    print("DEZEMBRO")
else:
    print("Mês inválido")