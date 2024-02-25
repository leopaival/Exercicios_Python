num = int(input("Digite um número inteiro: "))
print("Qual sera a base de conversão\nDigite {1} para binario \nDigite {2} para octal \nDigite {3} para hexadecimal:")
opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"{num} convertido para binario é igual a {bin(num)[2:]}") #colocou esse [2:] para contar só a partir do 2
elif opcao == 2:
    print(f"{num} convertido para octal é igual a {oct(num)[2:]}")  #pois os 2 primeiros nao precisa aparecer
elif opcao == 3:
    print(f"{num} convertido para hexadecimal é igual a {hex(num)[2:]}")
else:
    print("OPÇÃO INVÁLIDA. Tente novamente!")