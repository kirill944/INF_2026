from math import *
with open("27_А.txt") as file:
    a = file.read().replace(",", ".").split("\n")

def f(cluster):
    return min(cluster, key=lambda p: sum(dist(p, q) for q in cluster))


cluster1 = []
cluster2 = []
red1 = []
red2 =[]

for i in a:
    t = i.split()
    x, y, s = float(t[0]), float(t[1]), t[2]
    if x>10:
        cluster1.append([x * 10000, y * 10000])
        if s[0] == 'Y' and s[-3:] == 'III':
            red1.append([x * 10000, y * 10000])
    else:
        cluster2.append([x * 10000, y * 10000])

minn = 10000000
for i in cluster1:
    for j in cluster2:
        x1, y1 = i
        x2, y2 = j

        minn = min(minn, dist([x1, y1], [x2, y2]))

print(minn)
c1 = f(cluster1)
c2 = f(cluster2)
print(c1, c2)
print(224054 + 29111, 388882 + 343808)