lista = []
for c in range(0,3):
    n1 = str(input("Digite seu nome: "))
    lista.append(n1)
    if 'van' in lista:
        print("NOME IRREGULA, digite outro")
        lista.remove('van')
        n1 = str(input("Digite seu nome: "))
        lista.append(n1)



tudo = ''.join(lista)
print(len(lista[0]))
print(lista)
print(tudo)