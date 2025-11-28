t = int(input())
for i in range(t):
    k = int(input())
    local = 0
    visitant = 0
    for i in range(k):
        equip, punts = input().split()
        punts = int(punts)
        if equip == 'L':
            local += punts
        else:
            visitant += punts
    if local > visitant:
        print("L", local, visitant)
    elif visitant > local:
        print("V", local, visitant)
    else:
        print("E", local, visitant)