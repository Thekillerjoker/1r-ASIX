a = 33
b = 200
if b > a:
    print("b es major que a")
#Si el resultado es true mostrara el mensaje si es false no mostrara nada porqe no le has indicado que hacer si el resultadoes false

#Elif permite comprobar una condicion adiccional si la condicion primera no se cumple.
a = 33
b = 33
if b > a:
    print("B es major que a")
elif a == b:
    print("A es igual que b")
# Mostrara la seguda
a = 33
b = 33
if b >= a:
    print("B es major que a")
elif a == b:
    print("A es igual que b")
# Mostrara la primera ya que a la segunda no llega siempore mira el primero que se cumple 

# Else
a = 200
b = 33
if b > a:
    print("Be es major que a")
elif a == b:
    print("A i B son iguals")
else:
    print("A es diferent de b")
#Estro mostrara la tercera ya que ninguna de las primeras se muesrta

# And
edad = 25
tiene_carnet = True
if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir.")

# Condicion negativa:
es_fin_de_semana = False
if not es_fin_de_semana:
    print("Toca trabajar!!")

# Python Match:
day = 4
match day:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
