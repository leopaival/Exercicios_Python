frase = "Curso em Video Python"
print(frase[9:19])
print(len(frase))
print(frase.count('o'))
print(frase.count("o", 0, 13))
print(frase.find("deo"))
# frase.find("Android") quando coloca pra verificar uma palavra que nao existe, volta -1
print("Curso" in frase)

#Transformação
frase.replace("Python", "Android") #trocar palavra python por android
print(frase.replace("Python","Android"))
frase.upper() #deixar tudo maiusculo
frase.lower() #deixar tudo minusculo
frase.capitalize() #So aprimeira letra fica maiuscula
frase.title() #As primeiras letras de todas as palavras ficam maiusculas
frase.strip() #remove todos os espaços inuteis do começo e do final da string
frase.rstrip() #remove somente os ultimos espacos (os da direita)
frase.lstrip() #remove os espaços da esquerda

#Divisão
frase.split() #Ocorre uma divisao dentro da string considerando os espaços
print(frase.split())
nova = frase.split()
"".joinfrase # Para juntar todos os elementos
