def calcular_ir():
    salario = float(input("Salário bruto: "))
    dependentes = int(input("Número de dependentes: "))
    pensao = float(input("Valor da pensão: "))
    idoso = input("Tem 65 anos ou mais? (s/n): ").lower() == 's'

   
    # CÁLCULO INSS PROGRESSIVO
    inss = 0
    restante = salario

    faixas_inss = [
        (1518.00, 0.075),
        (2793.88, 0.09),
        (4190.83, 0.12),
        (8157.41, 0.14)
    ]

    anterior = 0
    detalhes_inss = []

    for limite, aliquota in faixas_inss:
        if salario > anterior:
            base = min(salario, limite) - anterior
            valor = base * aliquota
            inss += valor
            detalhes_inss.append((aliquota, valor))
            anterior = limite

    # BASE DE CÁLCULO
  
    deducao_dep = dependentes * 189.59
    isencao_idoso = 1903.98 if idoso else 0

    base_ir = salario - inss - deducao_dep - pensao - isencao_idoso
    if base_ir < 0:
        base_ir = 0


    # IR PROGRESSIVO
 
    ir = 0
    anterior = 0

    faixas_ir = [
        (2259.20, 0),
        (2826.65, 0.075),
        (3751.05, 0.15),
        (4664.68, 0.225),
        (float('inf'), 0.275)
    ]

    detalhes_ir = []

    for limite, aliquota in faixas_ir:
        if base_ir > anterior:
            base = min(base_ir, limite) - anterior
            valor = base * aliquota
            ir += valor
            detalhes_ir.append((aliquota, valor))
            anterior = limite

    # SALÁRIO LÍQUIDO

    liquido = salario - inss - ir - pensao


    # SAÍDA

    print("\n==============================")
    print(" CONTRACHEQUE – IR 2025")
    print("==============================")

    print(f"\nSalário bruto:     R$ {salario:.2f}")

    print(f"\n(-) INSS:          R$ {inss:.2f}")
    for aliq, val in detalhes_inss:
        print(f"  Faixa {aliq*100:.1f}%:     R$ {val:.2f}")

    print(f"\n(-) Dependentes:   R$ {deducao_dep:.2f}")
    print(f"(-) Pensão:        R$ {pensao:.2f}")
    print(f"(-) Isenção 65+:   R$ {isencao_idoso:.2f}")

    print(f"\nBase de cálculo:   R$ {base_ir:.2f}")

    print(f"\n(-) IR:            R$ {ir:.2f}")
    for aliq, val in detalhes_ir:
        if aliq > 0:
            print(f"  Faixa {aliq*100:.1f}%:     R$ {val:.2f}")
        else:
            print(f"  Faixa isenta:    R$ {val:.2f}")

    print("\n==============================")
    print(f"Salário líquido:   R$ {liquido:.2f}")
    print("==============================")


# Executar
calcular_ir()