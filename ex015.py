dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos Km rodados? "))
pago = dias*60 + 0.15*km
print(f"O total a pagar é de R${pago:.2f}")