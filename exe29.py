# Leia um número, calcule o fatorial deste número e mostre o resultado

numero = int(input("Informe um número: "))
fatorial = 1
contador = 2

while (contador <= numero):
    fatorial = fatorial * contador
    contador += 1
else:
    print(f"O valor do fatorial é de {fatorial}")