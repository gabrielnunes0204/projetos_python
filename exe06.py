#Crie um algoritmo que peça a altura e o peso de uma pessoa. Calcule e informe o IMC.

nome = input("Informe o seu nome: ")
peso = float(input("Informe o seu peso: "))
altura = float(input("Informe o seu altura: "))
imc = peso / (altura * altura)

if imc < 18:
    print(f"Olá {nome}, seu IMC é de {imc:.2f}, e você está ABAIXO DO PESO")
elif imc > 18 and imc < 24.9:
    print(f"Olá {nome}, seu IMC é de {imc:.2f}, e você está no PESO NORMAL")
elif imc > 24.9 and imc < 30:
    print(f"Olá {nome}, seu IMC é de {imc:.2f}, e você está com SOBREPESO")
elif imc > 30:
    print(f"Olá {nome}, seu IMC é de {imc:.2f}, e você está OBESO")
else:
    print("Olá {nome}, seu IMC não é válido")