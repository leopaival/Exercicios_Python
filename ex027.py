nome = str(input("Digite seu nome completo: ")).strip()
dividido = nome.split()
print(f"Seu primeiro nome é {dividido[0]}")
print(f"Seu ultimo nome é {dividido[-1]}") #maneira diferente de pegar o ultimo nome
print(f"Seu ultimo nome é {dividido[len(dividido)-1]}") #maneira diferente de pegar o ultimo nome

