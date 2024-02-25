valorcasa = float(input("Qual o valor da casa: "))
salario =  float(input("Qual o seu salário: "))
anos = int(input("Em quantos anos pretende pagar: "))
prestacao = valorcasa / (anos*12)
minimo = salario * 30 / 100
print(f"Para pagar uma casa de R${valorcasa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}")
if prestacao <= minimo:
    print("Emprestimo pode ser concedido!!!")
else:
    print("Emprestimo negado!!")
