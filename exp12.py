#ler 6 numeros e somar os pares
s = 0
for x in range(1, 7):
    n = int(input(f"Informe o {x}º numero: "))
    if(n%2 == 0):
        s += n
    else:
        continue
print (s)