lado1 = float(input("Digite o comprimento da primeira reta: "))
lado2 = float(input("Digite o comprimento da segunda reta: "))
lado3 = float(input("Digite o comprimento da terceira reta: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("As retas podem formar um triângulo.")
    if (lado1==lado2 and lado2 == lado3):
        print("Equiláterio")
    elif (lado1!=lado2 and lado2 != lado3 and lado1!=lado3):
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("As retas não podem formar um triângulo.")