n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2
print(f"tirando {n1} e {n2}, a media do aluno é {media}")
if media >= 5 and media < 7:
    print("O aluno está em RECUPERAÇÃO.")
elif media < 5:
    print("O aluno está REPROVADO.")
else:
    print("Aluno está APROVADO.")