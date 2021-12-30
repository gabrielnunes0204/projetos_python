#Leia três valores (A, B e C). Informe se A+B é maior do que C.

n1 = int(input("Informe o 1º valor: "))
n2 = int(input("Informe o 2º valor: "))
n3 = int(input("Informe o 3º valor: "))
soma = n1 + n2

if soma > n3:
    print(f"A soma de {n1} e {n2} é maior que {n3} - Soma {soma}")
else:
    print(f"A soma de {n1} e {n2} não é maior que {n3} - Soma {soma}")
    