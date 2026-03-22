def calcular_estacionamento():
    entrada = int(input("Hora de entrada (0-23): "))
    saida = int(input("Hora de saída (0-23): "))
    placa_final = int(input("Último número da placa: "))
    dia = input("Dia da semana: ").lower()

    # Validação básica
    if entrada < 0 or entrada > 23 or saida < 0 or saida > 23:
        print("Horário inválido")
        return

    # Cálculo das horas considera virada de dia
    if saida >= entrada:
        horas = saida - entrada
    else:
        horas = (24 - entrada) + saida

    # Mínimo de 1 hora
    if horas == 0:
        horas = 1

    # Tarifa base
    if horas >= 1:
        total = 10 + (horas - 1) * 5
    else:
        total = 10

    tarifa_base = total

    # Adicional noturno (22h às 6h)
    adicional_noturno = 0
    if entrada >= 22 or saida <= 6 or (entrada > saida):
        adicional_noturno = total * 0.5
        total += adicional_noturno

    # Desconto segunda-feira e placa par
    desconto = 0
    if dia == "segunda" and placa_final % 2 == 0:
        desconto = total * 0.10
        total -= desconto

    # Saída para o cliente
    print("\n Estacionamento")
    print(f"Entrada: {entrada:02d}h | Saída: {saida:02d}h")
    print(f"Permanência: {horas} horas")
    print(f"Tarifa base: R$ {tarifa_base:.2f}")

    if adicional_noturno > 0:
        print(f"Adicional noturno (50%): R$ {adicional_noturno:.2f}")

    if desconto > 0:
        print(f"Desconto (10%): -R$ {desconto:.2f}")

    print(f"Total: R$ {total:.2f}")


# Executar
calcular_estacionamento()