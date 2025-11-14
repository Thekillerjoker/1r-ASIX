casos = int(input())
for i in range(casos):
    vida,dany = map(int, input().split())
    if dany >= vida:
        print("Nope")
    elif dany > vida * 0.2:
        print("Momento Banana")
    else:
       print("Nope")
# Aqui lo que haces es casso te pide un numero,Luego en for i in range(casos): es que el bucle lo repetira el numeor de veces del valor de cassos,
# es decir si es tres repetira el bucle tres veces, bie en vida,dany= map(int, input().split)) es que los valores vida y any con map te convierte todo en int ya que lo indicas y que el valor de vida y dany es lo que introduzaca el usuario
#y slpit es que te separa estos valores en la misma linea, y con if dany >= vida: es si el valor de dany es mayor o igual a la vida mueres
# luego hace si dany es mas grande al 20% de la vida es decir no es mas grande que el 100% solo que el 20% enotnces te da la bannana
# y por ultimo el else te dice si no es ninguno de estos casos entoces Nope por ejemplo si pones 0 o algo asi
# entonces con el for i in range(casos) lo que haria es hacer los if el numero del valor en casos.
