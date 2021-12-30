# Solicite o nome, e-mail, rg e cpf da pessoa. Faça uma validação simples para verificar se todos os campos foram preenchidos.

nome = input("Informe o seu nome: ")
email = input("Informe o seu e-mail: ")
rg = int(input("Informe o seu RG (sem traços ou pontos): "))
cpf = int(input("Informe o seu CPF (sem traços ou pontos): "))

if nome == "":
    print("O campo de nome está vazio, preencha-o")
elif email == "":
    print("O campo de e-mail está vazio, preencha-o")
elif rg == "":
    print("O campo de RG está vazio, preencha-o")
elif cpf == "":
    print("O campo de CPF está vazio, preencha-o")
else:
    print("Todos os campos foram preenchidos corretamente. Obrigado")