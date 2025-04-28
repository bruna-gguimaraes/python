import random

def jogar_adivinhacao():
    print("Bem-vindo ao jogo de Adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = input("Digite um número entre 1 e 100 (ou 'sair' para encerrar): ")
        if tentativa.lower() == 'sair':
            print("Jogo encerrado. Obrigado por jogar!")
            break

        if not tentativa.isdigit():
            print("Por favor, digite um número válido.")
            continue

        tentativa = int(tentativa)
        tentativas += 1

        if tentativa < numero_secreto:
            print("Muito baixo. Tente novamente.")
        elif tentativa > numero_secreto:
            print("Muito alto. Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break

if __name__ == "__main__":
    jogar_adivinhacao()
1