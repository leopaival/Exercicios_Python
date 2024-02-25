from math import sin, cos, tan,radians
an = float(input("Digite um angulo qualquer: "))
seno = sin(radians(an))
cose = cos(radians(an))
tang = tan(radians(an))
print(f"O angulo digitado foi {an}, seu seno é {seno:.2f}, cosseno é {cose:.2f} e a tangente é {tang:.2f}")