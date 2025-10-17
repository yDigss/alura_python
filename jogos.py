print("*"*21)
print("Escolha o seu jogo!")
print("*"*21)

print("1 - Forca \n2 - Adivinhação")
jogo = eval(input("Qual a sua escolha?: "))

if jogo == 1:
    print("Jogando forca...")

elif jogo == 2:
    print("Jogando adivinhação...")

else:
    print("Opção inválida!")