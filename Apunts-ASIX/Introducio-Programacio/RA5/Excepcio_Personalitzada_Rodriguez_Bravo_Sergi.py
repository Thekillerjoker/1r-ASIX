class NombreNoPositiuException(Exception):
    pass
def llegirNombrePositiu():
    nombre = float(input("Introdueix un nombre positiu: "))
    if nombre <= 0:
        raise NombreNoPositiuException("Error: els nombres han de ser positius")
    return nombre
try:
    num1 = llegirNombrePositiu()
    num2 = llegirNombrePositiu()
    num3 = llegirNombrePositiu()
    suma = num1 + num2 + num3
    print("Suma final:", suma)
except NombreNoPositiuException as error:
    print(error)