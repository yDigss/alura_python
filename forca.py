import random

def introducao():
    print("*" * 28)
    print("Bem-Vindo ao jogo de Forca!")
    print("*" * 28)

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")

    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    lista = ["_" for letra in palavra]

    return lista

def seu_chute():
    chute = input("Qual letra? ").strip().lower()

    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    i = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[i] = letra
        i += 1

def mensagem_vencedor():
    print("Parabéns, Você ganhou!")

def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")

def desenha_forca(erros):
    if erros == 0:
        print("""
             _______
            |/      
            |      
            |      
            |       
            |      
            |
            |___
                """)
    elif erros == 1:
        print("""
             _______
            |/      |
            |      (_)
            |      
            |       
            |      
            |
            |___
                """)
    elif erros == 2:
        print("""
             _______
            |/      |
            |      (_)
            |       |
            |       |
            |      
            |
            |___
                """)
    elif erros == 3:
        print("""
             _______
            |/      |
            |      (_)
            |      \\|
            |       |
            |      
            |
            |___
                """)
    elif erros == 4:
        print("""
             _______
            |/      |
            |      (_)
            |      \\|/
            |       |
            |      
            |
            |___
                """)
    elif erros == 5:
        print("""
             _______
            |/      |
            |      (_)
            |      \\|/
            |       |
            |      / 
            |
            |___
                """)
    elif erros == 6:
        print("""
             _______
            |/      |
            |      (_)
            |      \\|/
            |       |
            |      / \\
            |
            |___
                """)

def jogar_forca():

    introducao()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = seu_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        mensagem_vencedor()

    else:
        mensagem_perdedor(palavra_secreta)


if __name__ == "__main__":
    jogar_forca()