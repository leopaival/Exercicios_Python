# Nesse exemplo o numero digitado não pode ultrapassar 4 caracteres
'''num = int(input("Informe um número: "))
n = str(num)
print(f"A Unidade é {n[3]}")
print(f"A Dezena é {n[2]}")
print(f"A Centena é {n[1]}")
print(f"A Milhar é {n[0]}")'''

num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"A Unidade é {u}")
print(f"A Dezena é {d}")
print(f"A Centena é {c}")
print(f"A Milhar é {m}")