#emprestimo
x = float(input("Valor da casa: "))
y = float(input("valor do Salario: "))
z = int(input("Em quantos anos pretende pagar? "))
prest = (x/ (z*12))
porc = y*0.3
if (prest <= porc):
    print("Emprestimo aprovado")
else:
    print("Emprestimo negado")
