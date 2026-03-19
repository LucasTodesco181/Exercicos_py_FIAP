def desconto(compra, vip):
    compra = float(compra)

    if compra <= 100:
        desc = 0
    elif compra <= 300:
        desc = 0.10
    elif compra <= 500:
        desc = 0.15
    else:
        desc = 0.20


    if vip.lower() == "sim":
        desc_vip = 0.05
    else:
        desc_vip = 0


    valor_desconto = compra * desc
    valor_vip = compra * desc_vip
    valor_final = compra - valor_desconto - valor_vip


    print("\n=== Resumo da Compra ===")
    print(f"Valor original: R$ {compra:.2f}")
    print(f"Desconto: R$ {valor_desconto:.2f}")
    print(f"Desconto VIP: R$ {valor_vip:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")


compra = float(input("Digite o valor da compra: "))
vip = input("Cliente é VIP? (sim/nao): ")

desconto(compra, vip)