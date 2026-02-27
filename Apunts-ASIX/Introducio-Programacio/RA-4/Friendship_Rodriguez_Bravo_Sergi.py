t = int(input())
for i in range(t):
    k = int(input())
    amics = {}
    for x in range(k - 1):
        persona, amic = input().split()
        amics[persona] = amic
    consulta = input()
    print(amics[consulta])