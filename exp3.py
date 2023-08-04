#alistamento
x = int(input("Em qual ano você nasceu?"))
ano_atual = 2023
idade = ano_atual - x

if (idade > 18):
    diferensa = (idade - 18)
    print(f"Já passou do periodo de se alistar o total de {diferensa} anos")
elif(idade == 18):
    print("Está na hora de você se alistar")
else:
    diferensa = (18 - idade)
    print(f"Ainda não é hora de se alistar, porém faltam {diferensa} anos")