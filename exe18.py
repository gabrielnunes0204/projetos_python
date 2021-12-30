# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.

altura = float(input("Informe a sua altura: "))
peso = float(input("Informe a sua peso: "))

imc = peso / (altura * altura)

if imc < 18:
    print(f"Seu IMC é de {imc:.2f}, e você está ABAIXO DO PESO")
elif imc >= 18.5 and imc < 24.9:
    print(f"Seu IMC é de {imc:.2f}, e você está com PESO NORMAL")
elif imc >= 24.9 and imc <= 29.9:
    print(f"Seu IMC é de {imc:.2f}, e você está com SOBREPESO")
elif imc >= 29.9 and imc < 34.9:
    print(f"Seu IMC é de {imc:.2f}, e você está com OBESIDADE GRAU I")
elif imc >= 34.9 and imc < 39.9:
    print(f"Seu IMC é de {imc:.2f}, e você está com OBESIDADE GRAU II")
elif imc > 39.9:
    print(f"Seu IMC é de {imc:.2f}, e você está com OBESIDADE GRAU III")
else:
    print("Seu IMC é inválido")