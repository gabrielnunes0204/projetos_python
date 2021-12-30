#Leia um número de 1 a 10, calcule e mostre a tabuada.

valor = int(input("Informe um valor para ver sua tabuada: "))
contador = 1

while(contador <= 10):
    print(valor, "X", contador, "=", (valor*contador))
    contador += 1