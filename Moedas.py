def conversor_moedas(valor, cotacao_euro=5.55, cotacao_dolar=5.15, cotacao_libra=6.45):
    valor = float(valor)

    euro = valor * cotacao_euro
    dolar = valor * cotacao_dolar
    libra = valor * cotacao_libra

    return euro, dolar, libra


valor = float(input('Digite um valor em real: '))

dados = conversor_moedas(valor)

print('Os valores convertidos são:')
print(f'Euro: {dados[0]:.2f}')
print(f'Dólar: {dados[1]:.2f}')
print(f'Libra: {dados[2]:.2f}')