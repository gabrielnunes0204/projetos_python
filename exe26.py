# Leia um número, depois calcule e mostre a tabuada.

numero = int(input("Informe um número de 1 a 10: "))
contador = 1

while(contador <= 10):
    print(numero, "x", contador, "=", (numero*contador))
    contador += 1
else:
    print("Fim da tabuada")