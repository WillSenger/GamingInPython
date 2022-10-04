import random

def bem_vindo():
    print("---------------------------------------")
    print("Bem vindo ao meu jogo da forca!")

def ler_lista():
    arquivo = open("Palavras.txt", "r")
    palavras_list = []

    for linha in arquivo:
        linha = linha.strip()
        palavras_list.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras_list))
    palavra = palavras_list[numero].upper()

    return palavra

def start_letras(palavra):
    return ["_" for letra in palavra]

def declara_letra():
    tentativa = input("Qual letra você quer tentar? ")
    tentativa = tentativa.strip().upper()
    return tentativa

def marca_tentativa(tentativa, letras_, palavra):
    index = 0
    for letra in palavra:
        if (tentativa == letra):
            letras_[index] = letra
        index += 1

def mensagem_winner():
    print("Você ganhou!")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣥⣤⣾⠟⡛⠿⠿⣭⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣽⡟⡏⢩⣦⡝⠋⢸⣶⠄⢲⡟⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣌⡳⣜⢿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⡛⢌⢿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄⠙⠌⣸⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⡿⠉⠉⠉⠉⢿⣿⣿⣿⠏⠉⠉⠉⠉⠉⠆⠄⠁⠄⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⡗⠫⠿⠆⠄⠸⢿⣿⣿⠂⠒⠲⡿⠛⠛⠂⠄⠄⢠⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⡛⣧⡔⠢⠴⣃⣠⣼⣿⣧⡀⠘⢢⣀⠄⠄⠄⠄⠄⢈⠁⢿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠄⠄⠄⣸⠆⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣼⢿⣿⣿⣿⣿⡀⠄⠘⡀⢠⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⡌⠿⣫⣿⣦⠬⢭⣥⣶⣬⣾⣿⢿⣿⡟⠄⢀⣿⣶⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣧⠘⣉⠛⢻⣛⣛⣛⣻⡶⠮⠙⠃⣉⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⡆⠸⣿⣶⢾⣿⣯⣤⣄⣀⣾⡟⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⠟⠿⠿⠿⠿⢿⣷⠄⣿⣿⣎⣹⢻⣿⣿⡿⡿⠁⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⠄⠄⠄⠄⠄⠄⠄⣠⠘⣿⣿⣿⣿⣿⣿⡟⠁⣀⣀⣀⠄⠘⠿⣿⣿⣿⣿⣿⣿⣿")

def mensagem_loser(palavra):
    print("Você perdeu!")
    print(f"A palavra era {palavra}")
    print("⣿⣿⡿⠋⠄⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠛⠲⣽⡛⢿⣿⣿⣿ ⣿⣿⣿ ⣿")
    print("⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⢦⡙⣿⣿ ⣿⣿⣿ ⣿")
    print("⣿⠇⠄⠄⣀⣠⣴⣶⣿⣿⣿⣿⣶⣶⣄⣀⠄⠄⠄⠄⠄⠄⠈⢯⣿ ⣿⣿⣿ ⣿")
    print("⡿⠄⠄⠘⠛⠛⠛⢿⣿⣿⡿⠛⠛⠛⠋⠉⢵⣦⣄⠄⠄⠄⠄⠄⢻ ⣿⣿⣿ ⣿")
    print("⠁⠄⠄⠄⠄⠄⠄⠄⢀⣠⡆⠄⠄⠄⠄⠄⠄⠄⠙⣳⣦⠄⠄⠄⠄ ⣿⣿⣿ ⣿")
    print("⣇⠄⠄⠄⠄⠄⠄⠄⣾⣿⣧⡀⠄⠄⠄⠄⠄⠄⣀⣿⣿⡇⠄⠄⠄ ⣿⣿⣿ ⣿")
    print("⣿⣿⣤⣤⣤⡀⠤⢾⣿⣿⡿⣿⣦⣤⣤⣤⣤⣶⣿⣿⣿⣿⣤⢀⣾ ⣿⣿⣿ ⣿")
    print("⣿⣿⣿⣿⣿⡿⠆⢀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣠⣿⠿⠿⢿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⠋⠁⢀⣈⣉⣩⣭⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣠⡶⢶⣆⢹⣿⣿")
    print("⣿⣿⣿⣿⣿⣷⣤⡘⠛⠶⢿⣿⣿⠶⠞⠋⠄⠄⠉⠛⢿⣿⠰⣿⣆⣙⣋⣼⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⢇⠻⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣶⣌⠻⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⣷⡌⢻⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⠄⠄⢸⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⡄⢿⣿")
    print("⣿⣿⣿⣿⣿⣿⣦⣤⣿⣧⣀⣴⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣾⣿⣿⡿⠁⣾⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⡘")

def jogar():
    bem_vindo()
    palavra = ler_lista()
    letras_ = start_letras(palavra)

    print(letras_)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        tentativa = declara_letra()

        if(tentativa in palavra):
            marca_tentativa(tentativa, letras_, palavra)
        else:
            erros += 1
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_
        print(letras_)

    if(acertou):
        mensagem_winner()
    else:
        mensagem_loser(palavra)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__=="__main__"):
    jogar()