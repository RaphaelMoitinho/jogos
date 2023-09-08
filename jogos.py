import adivinhacao
import forca

separar =  "******************************************************************"
iniciar =  "###---      Iniciando o jogo em:   3...   2...   1...       ---###"
escolher = "######----               Escolha o seu jogo             ----######"
jogar = "(1) Forca\n(2) Adivinhação"


def iniciar_jogo(jogo):
    print(separar)
    print(iniciar)
    print(separar)
    match jogo:
        case 1:
            forca.jogar()
        case 2:
            adivinhacao.jogar()

def escolher_jogo():
    print(separar)
    print(escolher)
    print(separar)
    print(jogar)
    print(separar)

def opção_invalida():
    print(separar)
    print("Escolha uma das opções disponiveis!")
    escolher_jogo()

escolher_jogo()
jogo_escolhido = 0

while True:
    jogo_escolhido = int(input("Qual o jogo deseja jogar?"))

    if(jogo_escolhido == 1):
        iniciar_jogo(1)

    elif(jogo_escolhido == 2):
        iniciar_jogo(1)

    else:
        opção_invalida()

if (__name__ == "__main__"):
    jogar()
