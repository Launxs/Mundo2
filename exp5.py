#idade
x = int(input("Em qual ano você nasceu?"))
ano_atual = 2023
idade = (ano_atual - x)
if (idade <= 9):
    print("Categoria Mirim")
elif(idade <= 14):
    print("Categoria Infantil")
elif(idade <= 19):
    print("Categoria Junior")
elif(idade <= 20):
    print("Categoria Sênior")
else:
    print("Categoria Master")