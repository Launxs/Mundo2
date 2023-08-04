#soma dos impares multiplos de 3
s = 0
contador = 0
for x in range(1, 501, 2):
    if(x%3 == 0):
        contador = contador +1
        s = s + x
print (f"a soma dos {contador} numeros é de: {s}")