casos = int(input())
for i in range(casos):
    vida,dany = map(int, input().split())
    if dany >= vida:
        print("Nope")
    elif dany > vida * 0.2:
        print("Momento Banana")
    else:
       print("Nope")
