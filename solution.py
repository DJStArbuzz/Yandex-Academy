a, b = map(int, input().split())
sp = []
for i in range(a):
    sp.append([int(i) for i in input().split()])
res = 0
for i in range(a - 1):
    for j in range(b - 1):
        if i == a - 1 and j != b - 1:
            res += sp[i][j]
        elif i != a - 1 and j == b - 1:
            res += sp[j][i]
        else:
            res += min(sp[i][j], sp[j][i])
        print(res)
print(res)
