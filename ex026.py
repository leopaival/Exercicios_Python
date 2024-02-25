frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A letra A aparece {frase.count('A')} vezes")
print(f"A primeira vez aparece na posição {frase.find('A')}")
print(f"A ultima vez que aparece é na posição {frase.rfind('A')}")
