k = int(input())
entrada = input().split()
n = int(input())
array = list(map(int, entrada))

for x in range(k):
    array[x] = array[x] + n
for x in range(k):
    print(array[x], end=" ")