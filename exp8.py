#pedra, papel ou tesousa
import random
from time import sleep
def jogar():
    print('-=-='*10)
    print("Bem-vindo ao jogo Pedra, Papel, Tesoura!")
    print("Escolha uma opção:")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    print('=-=-'*10)
    
    escolhas = ["Pedra", "Papel", "Tesoura"]
    jogador_escolha = int(input("Digite o número da sua escolha: "))
    jogador_escolha -= 1
    
    if jogador_escolha < 0 or jogador_escolha >= len(escolhas):
        print("Opção inválida. Tente novamente.")
        return
    
    jogador = escolhas[jogador_escolha]
    computador = random.choice(escolhas)
    
    print("Jo")
    sleep(0.5)
    print("Ken")
    sleep(0.5)
    print('Po!!!!!!')
    sleep(0.5)

    print ('-='*14)
    print("Você escolheu:", jogador)
    print("O computador escolheu:", computador)
    print ('-='*14)
    
    if jogador == computador:
        print("Empate!")
    elif (jogador == "Pedra" and computador == "Tesoura") or \
         (jogador == "Papel" and computador == "Pedra") or \
         (jogador == "Tesoura" and computador == "Papel"):
        print("Você venceu!")
    else:
        print("O computador venceu!")
        
jogar()
