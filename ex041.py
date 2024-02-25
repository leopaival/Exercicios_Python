from datetime import date
nasc = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - nasc
print(idade)

if idade <= 9:
    print("Classificação: Mirim")
elif 9 < idade <= 14:
    print("Classificação: Infantil")
elif 14 < idade <= 19:
    print("Classificação: Júnior")
elif 19 < idade <= 25:
    print("Classificação: Sênior")
else:
    print("Classificação: Master")