a = [int(i) for i in input().split()]
a = sorted(a)

rep = 0
for i in range(len(a)-1):
    if a[i+1] != a[i]:
        rep = 0
    elif a[i+1] == a[i] and rep == 0:
        print(a[i], end=' ')
        rep = 1


# Одно из решений
# ls = [int(i) for i in input().split()]
# for i in set(ls):
#     if ls.count(i) > 1:
#         print(i, end=' ')