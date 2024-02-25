from datetime import date
sexo = str(input("Qual seu sexo? M ou F? ")).upper().strip()

anoatual = date.today().year

if sexo == "M":
    ano = int(input("Ano de nascimento: "))
    idade = anoatual - ano
    print(f"Quem nasceu em {ano} tem {idade} anos em {anoatual}")
    if idade == 18:
        print("Você tem que se alistar IMEDIATAMENTE!!!")
    elif idade > 18:
        print(f"Você ja deveria ter se alistado ha {idade-18} anos")
        print(f"Seu alistamento foi em {anoatual- (idade-18)} ano")
    else:
        print(f"Voce ainda falta {18-idade} anos para o alistamento")
        print(f"Seu alistamento será em {18-idade + anoatual}")
elif sexo == "F":
    print("Mulheres não podem se alistar no Brasil")
else:
    print("Opção inválida!")