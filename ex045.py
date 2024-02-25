from random import randint
from time import sleep
print("Suas opções...\n[0] para PEDRA \n[1] para PAPEL \n[2] para TESOURA")
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input("Qual sua opção: "))
computador = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO!!')
sleep(1)
print('-='*15)
print(f"O computador escolheu {itens[computador]}")
print(f"O jogador escolheu {itens[jogador]}")
print('-='*15)
if computador == 0:
    if jogador == 0:
        print("EMPATOU")
    elif jogador == 1:
        print("Jogador GANHOU")
    elif jogador == 2:
        print("Computador Ganhou")
elif computador == 1:
    if jogador == 0:
        print("computador ganhou")
    elif jogador == 1:
        print("EMPATOU")
    elif jogador == 2:
        print("Jogador ganhou")
elif computador == 2:
    if jogador == 0:
        print("jogador ganhou")
    elif jogador == 1:
        print("computador ganhou")
    elif jogador == 2:
        print("empatou")



