# Uma fábrica de refrigerantes vende seu produto em três formatos: lata de 250 ml, garrafa de 500 ml e garrafa de 2 litros. Se um comerciante compra uma determinada quantidade de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou.

lata250 = int(input("Quantas latas de 250ml você comprou? "))
garrafa500 = int(input("Quantas garrafas de 500ml você comprou? "))
garrafaLitro = int(input("Quantas garrafas de 1 litro você comprou? "))

print(f"Você comprou {lata250} latas de refrigerante de 250ml, totalizando {lata250/4} litros")
print(f"Você comprou {garrafa500} garrafas de refrigerante de 500ml, totalizando {garrafa500/2} litros")
print(f"Você comprou {garrafaLitro} garrafas de refrigerante de 1 litro, totalizando {garrafaLitro/1} litros")
