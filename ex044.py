preco = float(input("Preço das compras: "))
print("FORMAS DE PAGAMENTO"
      "\n[1] à vista dinheiro/cheque"
      "\n[2] à vista no cartão"
      "\n[3] 2x no cartão"
      "\n[4] 3x ou mais no cartão")
opcao = int(input("Qual é a opção: "))

if opcao == 1:
    desconto = preco - preco*10/100
    print(f"Sua compra de R${preco:.2f} vai custar R${desconto:.2f} no final")
elif opcao == 2:
    desconto = preco - preco * 5 / 100
    print(f"Sua compra de R${preco:.2f} vai custar R${desconto:.2f} no final")
elif opcao == 3:
    desconto = preco / 2
    print(f"Sua compra de R${preco:.2f} dividido em 2x vai ficar 2X de R${desconto:.2f} no final")
elif opcao == 4:
    parcelas = int(input("Quantas parcelas: "))
    desconto = preco + preco * 20 / 100
    print(f"Sua compra será parcelada em {parcelas}x de R${desconto/parcelas:.2f} COM JUROS")
    print(f"Sua compra de R${preco:.2f} vai custar R${desconto:.2f} no final.")