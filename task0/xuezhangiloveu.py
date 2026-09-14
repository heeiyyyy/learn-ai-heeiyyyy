n = int(input())
namesdict = {}
for i in range(n):
    namesdict[i+1] = input().strip()
m = int(input())
for j in range(m):
    line = input()
    p = line.split()
    u = int(p[0])
    v = int(p[1])
    namesdict[u] = "I_love_"+namesdict[v]
print(namesdict[1])
