def jogar_forca():

    print("*"*28)
    print("Bem-Vindo ao jogo de Forca!")
    print("*"*28)

    palavra_secreta = "banana".lower()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input("Qual letra? ").strip().lower()

        if chute in palavra_secreta:
            i = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[i] = letra
                i += 1

        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        print("Você Ganhou!!")

    else:
        print("Você Perdeu!")

    print("Fim do Jogo!")

if __name__ == "__main__":
    jogar_forca()