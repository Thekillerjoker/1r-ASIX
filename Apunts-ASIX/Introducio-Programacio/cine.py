duracio, marge, hora, minut = map(int, input().split())

arribada = hora * 60 + minut
minuts_des_inici = arribada % duracio

if minuts_des_inici <= marge:
    print("VEURE")
else:
    print("MARXAR")