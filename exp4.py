#média
n1 = float(input("Informe o valor da primeira nota: "))
n2 = float(input("Informe o valor da segunda nota: "))
media = (n1+n2)/2
print(f"Sua media é {media}")
if (media>= 7):
    print ("Aprovado")
elif (media >= 5 and media <= 6.9):
    print("Recuperação")
else:
    print("Reprovado")