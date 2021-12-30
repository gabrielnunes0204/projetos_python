# Solicite um animal e mostre em inglês. (Ex.: gato, cachorro, etc..)

nomeAnimal = input("Informe o nome do animal: ")

if nomeAnimal == "cachorro":
    print("DOG")
elif nomeAnimal == "gato":
    print("CAT")
elif nomeAnimal == "passáro" or nomeAnimal == "passaro":
    print("BIRD")
elif nomeAnimal == "tubarão" or nomeAnimal == "tubarao":
    print("SHARK")
elif nomeAnimal == "peixe":
    print("FISH")
else:
    print("Nome ainda não registrado")