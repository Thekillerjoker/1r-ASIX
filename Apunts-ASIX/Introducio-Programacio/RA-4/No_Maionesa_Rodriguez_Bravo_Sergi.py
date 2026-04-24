casos = int(input())

for x in range(casos):
    dades = []
    
    dades.append(input())  
    dades.append(input())  
    dades.append(input())  

    parts = dades[0].split()
    temps = parts[0].split(":")
    h = int(temps[0])
    m = int(temps[1])
    periode = parts[1]

    if periode == "PM" and h != 12:
        h += 12
    if periode == "AM" and h == 12:
        h = 0

    inici = h * 60 + m

    parts = dades[1].split()
    temps = parts[0].split(":")
    h = int(temps[0])
    m = int(temps[1])
    periode = parts[1]

    if periode == "PM" and h != 12:
        h += 12
    if periode == "AM" and h == 12:
        h = 0

    final = h * 60 + m

    if final < inici:
        final += 24 * 60

    temps = dades[2].split(":")
    h = int(temps[0])
    m = int(temps[1])

    necesari = h * 60 + m

    if final - inici >= necesari:
        print("SI")
    else:
        print("NO")