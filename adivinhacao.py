import random

def jogar():
    separar = "******************************************************************"
    print(separar)
    print("######----       Bem vindo ao jogo de adivinhação!      ----######")
    print(separar)

    aleatorio = round(random.randrange(1,101))
    total_de_tentativas = 0
    nivel = 0
    chute = 0
    pontos = 100

    print(f"               Você tem {pontos} pontos disponiveis.             ")
    print(separar)

    print("Qual o nível de dificuldade?")
    print("(1) Fácil \n(2) Médio \n(3) Difícil")
    while True:
        nivel = int(input("Nível desejado: "))

        if (nivel == 1):
            total_de_tentativas = 20
            break
        elif (nivel == 2):
            total_de_tentativas = 10
            break
        elif (nivel == 3):
            total_de_tentativas = 5
            break
        else:
            print("Escolha um dos níveis abaixo:")
            print("(1) Fácil \n(2) Médio \n(3) Difícil")

    print(separar)
    print(f"O nível escolhido foi o {nivel}º e você tem {total_de_tentativas} tetativas. Boa sorte!")

    for rodada in range(0, total_de_tentativas):
        print(separar)
        print("Usando a {}ª tentativa".format(rodada+1))
        print(separar)

        valor_do_chute = input("Digite o seu numero entre 1 e 100: ")
        chute = int(valor_do_chute)

        if (chute < 1 or chute > 100):
            continue

        acertou          = chute == aleatorio
        errou_para_mais  = chute >  aleatorio
        errou_para_menos = chute <  aleatorio

        print(separar)
        print("Você digitou:", chute)
        print(separar)

        if(acertou):
            print("Você acertou!")
            break
        else:
            pontos -= abs(chute - aleatorio)
            if(errou_para_mais):
                print("Você errou! O seu chute foi maior que o numero secreto")
                print(f"Você tem {pontos} pontos disponiveis.")

            else:
                print("Você errou! O seu chute foi menor que o numero secreto")
                print(f"Você tem {pontos} pontos disponiveis.")

    print(separar)
    print(f"O numreo secreto é {aleatorio}")
    print(f"Você finalizou com {pontos} pontos.")
    print("Fim do jogo!")
    print(separar)

if (__name__ == "__main__"):
    jogar()