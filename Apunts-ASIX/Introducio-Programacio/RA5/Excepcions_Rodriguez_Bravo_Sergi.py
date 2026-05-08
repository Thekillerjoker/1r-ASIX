def dividir(a, b):
    if b == 0:
        raise Exception("No es pot dividir entre 0")
    return a / b


try:
    num1 = float(input("Introdueix el primer nombre: "))
    num2 = float(input("Introdueix el segon nombre: "))

    resultat = dividir(num1, num2)

    print("Resultat:", resultat)

except Exception as error:
    print("Error:", error)