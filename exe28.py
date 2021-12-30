# Leia o nome da pessoa. Caso ela deixe em branco solicite para digitar novamente.

nome = input("Informe o seu nome: ")

while nome == "":
    print("Informe o seu nome, por gentileza")
    nome = input("Informe o seu nome: ")
else:
    print("Obrigado")
