# Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar.
# Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais.
# Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real.

umCentavo = int(input("Quantas moedas de 1 centavo você tem? "))
cincoCentavos = int(input("Quantas moedas de 5 centavos você tem? "))
dezCentavos = int(input("Quantas moedas de 10 centavos você tem? "))
vinteCincoCentavos = int(input("Quantas moedas de 25 centavos você tem? "))
cinquentaCentavos = int(input("Quantas moedas de 50 centavos você tem? "))
umReal = int(input("Quantas moedas de 1 real você tem? "))

reaisUmCentavo = umCentavo/100
reaisCincoCentavos = cincoCentavos/20
reaisDezCentavos = dezCentavos/10
reaisVinteCincoCentavos = vinteCincoCentavos/4
reaisCinquentaCentavos = cinquentaCentavos/2
valorTotal = reaisUmCentavo + reaisCincoCentavos + reaisDezCentavos + reaisVinteCincoCentavos + reaisCinquentaCentavos + umReal

print(f"No total você tem {umCentavo} moedas de 01 centavo, e R$ {reaisUmCentavo:.2f}")
print(f"No total você tem {cincoCentavos} moedas de 05 centavos, e R$ {reaisCincoCentavos:.2f}")
print(f"No total você tem {dezCentavos} moedas de 10 centavos, e R$ {reaisDezCentavos:.2f}")
print(f"No total você tem {vinteCincoCentavos} moedas de 25 centavos, e R$ {reaisVinteCincoCentavos:.2f}")
print(f"No total você tem {cinquentaCentavos} moedas de 50 centavos, e R$ {reaisCinquentaCentavos:.2f}")
print(f"No total você tem {umReal} moedas de 01 real, e R$ {umReal:.2f}")
print(f"O valor total de moedas é de R$ {valorTotal}")
