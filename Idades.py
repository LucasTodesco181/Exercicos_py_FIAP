def defidor_de_idade(idade_em_anos: int, idade_em_meses: int = 0):
    idade_em_anos = int(idade_em_anos)
    idade_em_meses = int(idade_em_meses)

    if idade_em_meses < 0 or idade_em_meses > 12:
        return "Mês inválido"

    if idade_em_anos < 0 or idade_em_anos > 120:
        return "Idade inválida"
    elif idade_em_anos <= 11:
        return "Criança"
    elif idade_em_anos <= 17:
        return "Adolescente"
    elif idade_em_anos <= 59:
        return "Adulto"
    else:
        return "Idoso"


idade_em_anos = int(input('Digite sua idade: '))
idade_em_meses = int(input('Digite seus meses: '))

print(defidor_de_idade(idade_em_anos, idade_em_meses))

print('voce tem', idade_em_anos, 'anos e', idade_em_meses, 'meses')