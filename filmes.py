def exibir_menu():
    print("Escolha um gênero de filme para obter recomendações:")
    print("1. Ação")
    print("2. Comédia")
    print("3. Drama")
    print("4. Ficção Científica")
    print("5. Terror")
    print("6. Sair")

def recomendar_filmes(genero):
    filmes = {
        "Ação": ["Vingadores: Ultimato", "Mad Max: Estrada da Fúria", "John Wick", "Duro de Matar"],
        "Comédia": ["A Vida é Bela", "Superbad", "Se Beber, Não Case", "O Grande Lebowski"],
        "Drama": ["Forrest Gump", "O Poderoso Chefão", "A Lista de Schindler", "Clube da Luta"],
        "Ficção Científica": ["Matrix", "Interstellar", "Blade Runner 2049", "Star Wars: O Império Contra-Ataca"],
        "Terror": ["O Exorcista", "It: A Coisa", "Hereditary", "O Sexto Sentido"]
    }

    if genero in filmes:
        print(f"\nRecomendações de filmes no gênero {genero}:")
        for filme in filmes[genero]:
            print(f"- {filme}")
    else:
        print("Gênero inválido! Tente novamente.")

def main():
    while True:
        exibir_menu()
        escolha = int(input("\nDigite o número da opção desejada: "))
        
        if escolha == 1:
            recomendar_filmes("Ação")
        elif escolha == 2:
            recomendar_filmes("Comédia")
        elif escolha == 3:
            recomendar_filmes("Drama")
        elif escolha == 4:
            recomendar_filmes("Ficção Científica")
        elif escolha == 5:
            recomendar_filmes("Terror")
        elif escolha == 6:
            print("Obrigado por usar o recomendador de filmes! Até logo.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
