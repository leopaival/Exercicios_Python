from random import randint
from time import sleep
print("------JOGO DA ADVINHAÇÃO-----")
print("=== Sera que consegue adivinhar qual numero o computador está pensando??? ===")
print("Ele está pensando em um número de 0 a 5")
comp =  randint(0,5)
print(comp)
usuario = int(input("Qual foi o número escolhido pelo computador: "))
print("PENSANDO....")
sleep(3)
if usuario == comp:
    print("Parabens meu grande amigo, Voce ACERTOUUUUU!")
else:
    print("Não foi dessa vez, você ERROUUUU!")