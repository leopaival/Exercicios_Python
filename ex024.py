cidade = str(input("Em que cidade você nasceu: ")).upper().strip()
print("SANTO" in cidade) #Nesse caso verifica se tem santo na cidade mas pode ter o santo no final
dividido = cidade.split()
print("SANTO" in dividido[0]) #Nesse caso verifica o santo no começo
print(cidade[0:5] == "SANTO") #Nesse caso verifica o santo no começo
