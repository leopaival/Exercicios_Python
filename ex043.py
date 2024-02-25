peso = float(input("Qual é seu peso: "))
altura = float(input("Qual é sua altura: "))
imc = peso/altura**2
print(f"O IMC dessa pessoa é de {imc:.1f}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso Ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
elif imc >= 40:
    print("OBESIDADE MÓRBIDA")