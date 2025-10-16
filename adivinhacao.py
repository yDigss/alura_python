print("*"*33)
print("Bem-Vindo ao jogo de Adivinhação")
print("*"*33)

numero_secreto = 42
total_de_tentativas = 3

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
        print("Você acertou!")
        break

    else:
        if maior:
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif menor:
            print("Você errou! Seu chute foi menor que o número secreto.")


print("Fim do Jogo!")