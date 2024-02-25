salario = float(input("Qual é o salário do funcionário: "))

if salario > 1250.00 :
    novosalario = salario + salario*10/100
    print(f"Parabens seu salario teve um aumento de 10%, ficando em R${novosalario:.2f}")
else:
    novosalario = salario + salario*15/100
    print(f"Parabens seu salario teve um aumento de 15%, ficando em R${novosalario:.2f}")