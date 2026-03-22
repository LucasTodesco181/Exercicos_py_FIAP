def valor():
    saque = int(input("Digite um valor para o saque: "))

    if saque < 0:
        return "Valor inválido"
    elif saque % 10 != 0:
        return "valor não multiplo de 10"
    else:
        notas = [200, 100, 50, 20, 10]
        total = 0

        for cedula in notas:
            quantidade = saque // cedula
            total += quantidade
            saque = saque % cedula
            print(f'R${cedula}: total de cedulas: {quantidade}')

    print(f'Quantidade de cedulas utilizadas:{total}')

print("salve")
valor()