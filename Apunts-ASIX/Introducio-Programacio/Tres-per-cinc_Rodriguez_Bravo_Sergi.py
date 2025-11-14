a,b = map(int, input().strip().split())
resposta = ""
for i in range(b):
    resposta += str(a)
print(resposta)
#El map sirve para cojerte todo las dadas ded dentro y convertirlas a int   
# El resposta="" es lo que te va ha mostrar por eso entre ""
# for i in range(b): lo que te va hacer ess hacer bucle el rango b  es decir el numero que sea b
# y que es lo que va ha repetir pues lo que esta dentro del bucle es decir resposta += str(a) que lo que hace es hacer ubna suma pero que no es una suma sino que lo que hace es juntar el valor de a converitdo a str
# Es decir que  por ejemplo si b es 4 lo qye va ha hacer es junntar  4 veces el valor de a es decir si a es 3 juntara 4 veces 3 3333
