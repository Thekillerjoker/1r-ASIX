casos = int(input("Cuantos casos quieres? "))
for i in range(casos):
    operacion = input("Es transexual Si/No ? ")
    while operacion == "No":
        sexo = input("Eres Hombre o Mujer: ")
        if sexo == "Mujer":
            altura, pecho, cintura = map(int, input("Altura, Pecho Cintura: ").split())
            if altura < 160:
                print("Enana")
            # 108 cm de pecho, 160cm de altura, 70cm cintura.
            elif altura >= 160 and altura < 170 and pecho >= 108 and cintura >= 70:
                print("Ta buena")
                print(f"Altura: {altura}, Pecho: {pecho}, Cintura: {cintura}")
            else:
                print("No me sirve")
        if sexo == "Hombre":
            tula = float(input(" Cuanto te mide: "))
            if tula < 13.59:
                print(f"vaya mierda {tula}cm de tula")
            elif tula >= 13.59 and tula <= 16.5:
                print(f"Dentro de la media {tula}cm de tula")
            elif tula > 16.5 and tula <= 24.5:
                print(f"Tamos ready {tula}cm de tula")
            else:
                print(f"Baya Mounstruo pa {tula}cm de tula")
        operacion = input("Eres transxual Si/No ? ")
    if operacion == "Si":
        print("No me hables")