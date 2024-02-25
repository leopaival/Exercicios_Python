s = float(input("Qual é o salário do Funcionário? R$ "))
aumento = s + (s*15/100)
print(f"Um funcionário que ganhava R${s}, com 15% de aumento, passa a receber R${aumento:.2f}")