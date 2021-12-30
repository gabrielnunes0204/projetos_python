#Pergunte qual o valor da compra e a forma de pagamento, se for a vista dê 10% de desconto, caso contrário dê 5%.

valorCompra = float(input("Informe o valor da compra: "))
formaPagamento = input("Informe qual a forma de pagamento: ")
valorAVista = (valorCompra * 10) / 100
valorOutro = (valorCompra *  5) / 100

if formaPagamento == 'A Vista' or formaPagamento == 'a vista' or formaPagamento == 'À vista':
    print(f"O seu pagamento foi feita à vista, assim terá 10% de desconto na compra, ficando no valor de R$ {valorCompra-valorAVista}")
else:
    print(f"Você terá 5% de desconto na compra, ficando no valor de R$ {valorCompra-valorOutro}")

