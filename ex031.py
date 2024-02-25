distancia = float(input("Qual a distancia da viagem em KM: "))

if distancia <= 200:
    valor = distancia * 0.50
    print(f"Sua viagem foi de {distancia}Km e o valor foi de R${valor:.2f}")
else:
    valor = distancia * 0.45
    print(f"Sua viagem foi de {distancia}Km e o valor foi de R${valor:.2f}")