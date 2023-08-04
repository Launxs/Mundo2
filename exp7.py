#IMC
peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))
if(altura>5):
    alt = altura/100
    imc = (peso / alt**2)
    if (imc < 18.5):
        print (f"Seu imc é de: {imc:.4f} e você se enquadra no status: Abaixo do peso")
    elif (imc >= 18.5 and imc < 25):
        print (f"Seu imc é de: {imc:.4f} e você se enquadra no status: Peso ideal")
    elif (imc >= 25 and imc < 30):
        print (f"Seu imc é de: {imc:.4f} e você se enquadra no status: Sobrepeso")
    elif (imc >= 30 and imc <40):
        print (f"Seu imc é de: {imc:.4f} e você se enquadra no status: Obesidade")
    else:
        print (f"Seu imc é de: {imc:.4f} e você se enquadra no status: Obesidade morbida")
else:
    imc = (peso / altura**2)
    if (imc < 18.5):
        print (f"Seu imc é de: {imc:.4f} e você se enquadra no status: Abaixo do peso")
    elif (imc >= 18.5 and imc < 25):
        print (f"Seu imc é de: {imc:.4f} e você se enquadra no status: Peso ideal")
    elif (imc >= 25 and imc < 30):
        print (f"Seu imc é de: {imc:.4f} e você se enquadra no status: Sobrepeso")
    elif (imc >= 30 and imc <40):
        print (f"Seu imc é de: {imc:.4f} e você se enquadra no status: Obesidade")
    else:
        print (f"Seu imc é de: {imc:.4f} e você se enquadra no status: Obesidade morbida")