F = int(input())
edats = list(map(int, input().split()))
E = int(input())

no_mengen = 0
for edat in edats:
    if edat < E:
        no_mengen += 1
print(no_mengen)