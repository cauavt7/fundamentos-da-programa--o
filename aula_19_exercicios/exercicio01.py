
def calcular_media():
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    if nota1 < 0 or nota1 > 10:
        return -1.0

    if nota2 < 0 or nota2 > 10:
        return -1.0

    if nota3 < 0 or nota3 > 10:
        return -1.0

    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
    return round(media, 1)

print(calcular_media())