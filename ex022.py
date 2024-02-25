nome = str(input("Digite seu nome completo: ")).strip()
dividido = nome.split()
junto = "".join(dividido)
print(f"O nome com todas as letras maiúsculas é {nome.upper()}")
print(f"O nome com todas as letras minúsculas é {nome.lower()}")
print(f"A quantidade de letras sem contar espaços é de {len(junto)} letras")
print(f"Seu primeiro nome é {dividido[0]}")
print(f"E ele tem {nome.find(' ')} letras")

