f = [0] * 10010
for n in range(10000-1, 0, -1):
    if n >= 2024:
        f[n] = 1
    else:
        f[n] = f[n+2] + f[n+4]

#print(f)
g = list()
for i in f:
    if i!=0 and i not in g:
        g.append(i)
print(len(g))