n = input("Digite algo: ")
print(f"O tipo primitivo desse valor é {type(n)}")
print(f"só tem espacos? {n.isspace()}")
print(f"é um numero? {n.isnumeric()}")
print(f"é alfabetico? {n.isalpha()}")
print(f"é alfanumerico? {n.isalnum()}")
print(f"está em maiuscula? {n.isupper()}")
print(f"está em minuscula? {n.islower()}")
print(f"está capitalizada? {n.istitle()}")


