import random

def jogar():

    palavra_secreta = sortear_palavras("palavras.txt")
    palavra_secreta_lista = ["_" for letra in palavra_secreta]
    tentativas = 7
    enforcou = False
    acertou = False


    gerar_msg_abertura(palavra_secreta, palavra_secreta_lista, tentativas)
    validar_tentativas(palavra_secreta, palavra_secreta_lista, tentativas, acertou, enforcou)
    gerar_msg_encerramento()



def gerar_msg_abertura(palavra_secreta, palavra_secreta_lista, tentativas):
    print("**************************************************")
    print("######----  Bem vindo ao jogo da Forca! ----######")
    print("**************************************************")
    print(f"#-- Tente adivinhar a palavra que tem {len(palavra_secreta)} letras --#")
    print("**************************************************")
    print(f"#--     Você terá {tentativas} tentativas para acertar    --#")
    print("**************************************************")
    print(f"\n \n \n \n {palavra_secreta_lista}")

def sortear_palavras(nome_arquivo):
    palavras = []
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha.upper())

    i = random.randrange(0,len(palavras))
    palavra_sorteada = palavras[i]
    return palavra_sorteada

def validar_tentativas(palavra_secreta, palavra_secreta_lista, tentativas, acertou, enforcou):


    while (not enforcou and not acertou):

        chute = input("Qual a letra?").strip().upper()

        index = 0
        acertos = 0
        for letra in palavra_secreta:
            if (chute == letra):
                acertos += 1
                palavra_secreta_lista[index] = letra
            index += 1

        if (acertos > 0):
            print("**************************************************")
            print(f"#--     Encontramos {acertos} letras {chute} na palavra.     --#")
            print("**************************************************")
            desenha_forca(tentativas)

        else:
            print("**************************************************")
            print(f"#--  Não foi encontrada a letra {chute} na palavra.  --#")
            print("**************************************************")
            desenha_forca(tentativas)

        if (tentativas > 1):
            print(f"#--        Você ainda tem {tentativas-1} tentativas.        --#")
            print("**************************************************")

        print(palavra_secreta_lista)

        tentativas -= 1

        enforcou = tentativas == 0
        acertou = "_" not in palavra_secreta_lista

        gerar_msg_vencedor(acertou)
        gerar_msg_perdedor(palavra_secreta, enforcou)

def desenha_forca(tetativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tetativas == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tetativas == 6):
        print(" |      (_)   ")
        print(" |    ---     ")
        print(" |            ")
        print(" |            ")

    if(tetativas == 5):
        print(" |      (_)   ")
        print(" |    ---|    ")
        print(" |            ")
        print(" |            ")

    if(tetativas == 4):
        print(" |      (_)   ")
        print(" |    ---|--- ")
        print(" |            ")
        print(" |            ")

    if(tetativas == 3):
        print(" |      (_)   ")
        print(" |    ---|--- ")
        print(" |       |    ")
        print(" |            ")

    if(tetativas == 2):
        print(" |      (_)   ")
        print(" |    ---|--- ")
        print(" |       |    ")
        print(" |      /     ")

    if (tetativas == 1):
        print(" |      (_)   ")
        print(" |    ---|--- ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def gerar_msg_vencedor(acertou):
    if (acertou):
        print("**************************************************")
        print("######----   PARABÉNS VOCÊ GANHOU!      ----######")
        print("**************************************************")
        print("                   ___________                    ")
        print("                  '._==_==_=_.'                   ")
        print("                  .-\\:      /-.                  ")
        print("                 | (|:.     |) |                  ")
        print("                  '-|:.     |-'                   ")
        print("                    \\::.    /                    ")
        print("                     '::. .'                      ")
        print("                       ) (                        ")
        print("                     _.' '._                      ")
        print("                    '-------'                     ")

def gerar_msg_perdedor(palavra_secreta, enforcou):
    if (enforcou):
        print("**************************************************")
        print("A palavra secreta era {}".format(palavra_secreta))
        print("**************************************************")
        print("######----    Tentativas esgotadas      ----######")
        print("**************************************************")
        print("                  _____________                   ")
        print("                /               \                 ")
        print("              /                   \               ")
        print("              |   XXXX     XXXX   |               ")
        print("              |   XXXX     XXXX   |               ")
        print("              |   XXXX     XXXX   |               ")
        print("              \__      X X     __/               ")
        print("                | |           | |                 ")
        print("                | I I I I I I I |                 ")
        print("                  \_         _/                   ")
        print("                    \_______/                     ")

def gerar_msg_encerramento():
    print("**************************************************")
    print("######----        Fim do jogo!          ----######")
    print("**************************************************")

if (__name__ == "__main__"):
    jogar()