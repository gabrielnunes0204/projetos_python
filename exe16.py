# Crie um algoritmo que peça a altura e o peso de uma pessoa. Calcule o IMC e informe se ele está dentro do intervalo de 18,5 e 25.

altura = float(input("Informe a sua altura: "))
peso = float(input("Informe a seu peso: "))

imc = peso / (altura * altura)

if imc >= 18.5 and imc <= 25:
    print(f"Seu IMC é de {imc:.2f}, e você está no PESO IDEAL")
else:
    print(f"Seu IMC é de {imc:.2f}")