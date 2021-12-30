#Leia dois valores (A e B) e informe qual é o maior valor.

primeiroValor = int(input("Informe o 1° valor: "))
segundoValor = int(input("Informe o 2° valor: "))

if primeiroValor > segundoValor:
    print(f"O valor {primeiroValor} é maior que {segundoValor}, ou seja, o primeiro valor é maior")
elif primeiroValor < segundoValor:
    print(f"O valor {segundoValor} é maior que {primeiroValor}, ou seja, o segundo valor é maior")
else:
    print(f"Os valores {primeiroValor} e {segundoValor} são iguais")