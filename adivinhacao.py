import random

def jogar_adivinhacao():

    print("*"*33)
    print("Bem-Vindo ao jogo de Adivinhação")
    print("*"*33)

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) - Fácil\n(2) - Médio\n(3) - Difícil")
    nivel = eval(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 15

    elif nivel == 2:
        total_de_tentativas = 10

    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print(f"Tentativa: {rodada} de {total_de_tentativas}")

        chute_str = eval(input("Digite um número entre 1 e 100: "))
        print(f"Você digitou {chute_str}")
        chute = int(chute_str)

        if chute_str < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Você acertou! Conseguiu {pontos} pontos!")
            break

        else:
            if maior:
                print("Você errou! Seu chute foi maior que o número secreto.")
            elif menor:
                print("Você errou! Seu chute foi menor que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos


    print("Fim do Jogo!")