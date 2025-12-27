s = int(input())
etapa = s // 43200
dia = etapa // 2 + 1
if etapa % 2 == 0:
    print("mati del dia", dia)
else:
    print("nit del dia", dia)