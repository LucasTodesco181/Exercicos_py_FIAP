def calcular_imc(altura, peso):
    altura = float(altura)
    peso = float(peso)
    imc = peso / (altura ** 2)

    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc < 24.9:
        return 'Peso normal'
    elif imc >= 25.0 and imc < 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidade'


altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

resultado = calcular_imc(altura, peso)

print('Classificação:', resultado)
print("Peso:", peso, "| Altura:", altura)