from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
print(f"O comprimento da hypotenusa é de {hypot(co,ca):.2f}")