#Faça um algoritmo para uma loja de 1,99. Leia quantos itens foram vendidos. Conceda um desconto de 5% e informe o valor final.

itensVendidos = int(input("Informe quantos itens foram vendidos: "))
valorTotal = itensVendidos * 1.99
desconto = (valorTotal * 5) / 100

print(f"O valor dos itens vendidos é de R$ {valorTotal}, e com o desconto de 5% fica R$ {valorTotal-desconto}")