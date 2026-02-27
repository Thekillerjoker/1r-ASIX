n = int(input('Introdueix el numero de casos:' ))
dades = {}
for x in range(n):
    nom = input('Introdueix el nom:' )
    data = input('Introdueix la data:' )
    dades[nom] = data
consulta = input('Introdueix el nom a consultar:' )
elements = [f"{nom}={data}" for nom, data in dades.items()]
sortida = "{" + ", ".join(elements) + "}"
print(sortida)
print(dades[consulta])