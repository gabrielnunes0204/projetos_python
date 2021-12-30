# Sabendo que cada unidade de ferradura custa 9,90, pergunte quantos cavalos precisam de (4) ferraduras. Se o custo total for maior que 100, aplique um desconto de 10%. Depois informe o valor final. 

qtdCavalos = int(input("Quantos cavalos precisam de ferraduras? "))
valorTotal = (qtdCavalos * 9.90) * 4


if valorTotal > 100:
    valorDesconto = (valorTotal * 10) /100
    print(f"O valor total das ferraduras sem desconto é de R$ {valorTotal}")
    print(f"Mas você ultrapassou os R$ 100,00 e ganhou um desconto, sua compra agora fica no valor de R$ {valorTotal-valorDesconto}")
else:
    print(f"O valor total das ferraduras é de R$ {valorTotal}")


