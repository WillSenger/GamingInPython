import random

def jogar():

    print("---------------------------------------")
    print("Bem vindo ao meu jogo de adivinhação!")

    n = random.randrange(1, 101)
    total_tentativa = 0
    pontos = 100

    print("Em qual dificuldade você quer jogar?")
    print("1 - Fácil, 2 - Médio e 3 - Difícil.")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_tentativa = 8
    elif nivel == 2:
        total_tentativa = 5
    else:
        total_tentativa = 2

    for rodada in range (1, total_tentativa + 1):
        print(f"Tentativa {(rodada)} de {(total_tentativa)}")
        tentativa = int(input("Digite um número entre 1 e 100 para tentar adivinhar: "))
        print("Você digitou: ", tentativa)

        acertou = tentativa == n
        maior = tentativa > n
        menor = tentativa < n

        if tentativa < 1 or tentativa > 100:
            print("Você deve digitar um número entre 1 e 100!")

        if acertou:
            print("Você acertou o número e fez {} pontos:)".format(pontos))
            break
        else:
            if maior:
                print("Você errou o número! A sua tentativa foi maior que o número correto :(")
            elif menor:
                print("Você errou o número! A sua tentativa foi menor que o número correto :(")
            pontos_perdidos = abs(n - tentativa)
            pontos = pontos - pontos_perdidos

    print("O Jogo acabou!")

if (__name__=="__main__"):
    jogar()