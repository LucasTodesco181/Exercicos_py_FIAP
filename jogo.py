import random

def jogar():
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("4 - Lagarto")
    print("5 - Spock")

    jogador = int(input("Sua escolha: "))

    if jogador < 1 or jogador > 5:
        print("Opção inválida")
        return

    computador = random.randint(1, 5)

    opcoes = {
        1: "Pedra",
        2: "Papel",
        3: "Tesoura",
        4: "Lagarto",
        5: "Spock"
    }

    # Regras: (vencedor, perdedor): ação
    regras = {
        (1, 3): "quebra",
        (1, 4): "esmaga",
        (2, 1): "cobre",
        (2, 5): "refuta",
        (3, 2): "corta",
        (3, 4): "decapita",
        (4, 2): "come",
        (4, 5): "envenena",
        (5, 1): "vaporiza",
        (5, 3): "derrete"
    }

    print("\n Resultado")
    print(f"Você: {opcoes[jogador]}")
    print(f"Computador: {opcoes[computador]}")

    if jogador == computador:
        print("Empate")
        return

    # Verifica vencedor
    if (jogador, computador) in regras:
        acao = regras[(jogador, computador)]
        print(f"{opcoes[jogador]} {acao} {opcoes[computador]} — Você venceu!")
    else:
        acao = regras[(computador, jogador)]
        print(f"{opcoes[computador]} {acao} {opcoes[jogador]} — Computador venceu!")


# Executar
jogar()