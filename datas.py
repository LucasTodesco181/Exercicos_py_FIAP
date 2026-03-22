def verificar_data():
    dia = int(input("Qual é o dia?: "))
    mes = int(input("Qual é o mês?: "))
    ano = int(input("Qual é o ano?: "))

    # Verifica se é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        bissexto = True
    else:
        bissexto = False

    # Verifica mês válido
    if mes < 1 or mes > 12:
        print("Data inválida: mês não existe")
        return

    # Define dias por mês
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias_no_mes = 31
    elif mes in [4, 6, 9, 11]:
        dias_no_mes = 30
    elif mes == 2:
        dias_no_mes = 29 if bissexto else 28

    # Verifica dia válido
    if dia < 1:
        print("Data inválida: dia não existe")
        return

    if dia > dias_no_mes:
        print(f"Data inválida: este mês tem apenas {dias_no_mes} dias")
        return

    # Se passou por tudo
    print(f"\nData: {dia:02d}/{mes:02d}/{ano}")
    print("Ano bissexto:", "Sim" if bissexto else "Não")
    print("Data válida!")

# Executar
verificar_data()