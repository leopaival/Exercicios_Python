velo = float(input("Qual a velocidade do carro: "))

if velo > 80:
    multa = (velo - 80) * 7
    print("Voce acaba de ser multado!")
    print(f"Sua multa sera de R${multa:.2f}")
else:
    print("Velocidade normal")
print("Boa Viagem")