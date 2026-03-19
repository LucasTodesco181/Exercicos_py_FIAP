def classificar_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Não forma triângulo"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Não forma triângulo"

    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"


# Entrada de dados do usuário
a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

# Resultado
resultado = classificar_triangulo(a, b, c)

print(f"Resultado: {resultado}")