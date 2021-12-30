# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento

valorProduto = int(input("Informe o valor do produto: "))
formaPagamento = int(input("Informe a forma de pagamento (1...4): \n 1 - À vista em dinheiro ou cheque / \n 2 - À vista no cartão de crédito / \n 3 - Em duas vezes no cartão / \n 4 - Em seis vezes \n"))

primeiroDesconto = (valorProduto * 15) / 100
segundoDesconto = (valorProduto * 5) / 100
terceiroDesconto = (valorProduto * 10) / 100

if formaPagamento == 1:
    print(f"O valor total do produto é de R$ {valorProduto}, e com o desconto fica R$ {valorProduto-primeiroDesconto}")
elif formaPagamento == 2:
    print(f"O valor total do produto é de R$ {valorProduto}, e com o desconto fica R$ {valorProduto-segundoDesconto}")
elif formaPagamento == 3:
    print(f"O valor total do produto é de R$ {valorProduto}")
elif formaPagamento == 4:
    print(f"O valor total do produto é de R$ {valorProduto}, e com o desconto fica R$ {valorProduto-terceiroDesconto}")

