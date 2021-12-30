#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

nome = input("Informe o seu nome: ")
altura = float(input("Informe a sua altura: "))
sexo = input("Informe o seu sexo: ")

pesoIdealMasc = (72.7 * altura) - 58
pesoIdealFemi = (62.1 * altura) - 44.7

if sexo == "m" or sexo == "M":
    print(f"Olá {nome}, seu peso ideal é: {pesoIdealMasc}kg")
elif sexo == "f" or sexo == "F":
    print(f"Olá {nome}, seu peso ideal é: {pesoIdealFemi}kg")
else:
    print("Valor de sexo inválido")