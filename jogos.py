from adivinhacao import jogar_adivinhacao
from forca import jogar_forca

def escolhe_jogo():

    print("*"*21)
    print("Escolha o seu jogo!")
    print("*"*21)

    print("1 - Forca \n2 - Adivinhação")
    jogo = eval(input("Qual a sua escolha?: "))

    if jogo == 1:
        print("Jogando forca...")
        jogar_forca()

    elif jogo == 2:
        print("Jogando adivinhação...")
        jogar_adivinhacao()

    else:
        print("Opção inválida!")

if __name__ == "__main__":
    escolhe_jogo()