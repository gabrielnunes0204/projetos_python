# Solicite um número de 0 a 6 e informe o dia da semana por extenso.

dia = int(input("Informe o dia da semana por número (1...7): "))

if dia == 1:
    print("DOMINGO")
elif dia == 2:
    print("SEGUNDA-FEIRA")
elif dia == 3:
    print("TERÇA-FEIRA")
elif dia == 4:
    print("QUARTA-FEIRA")
elif dia == 5:
    print("QUINTA-FEIRA")
elif dia == 6:
    print("SEXTA-FEIRA")
elif dia == 6:
    print("SÁBADO")
else:
    print("Dia inválido")