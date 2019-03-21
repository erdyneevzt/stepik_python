ls = []
while True:
    a = [i for i in input().split()]
    if a[0] == 'end':
        break
    else:
        ls.append([int(i) for i in a])

row = len(ls)
col = len(ls[0])

a = [[0 for j in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        for di in [-1, 1]:
            index = (i + di - row) % row
            a[i][j] += ls[index][j]
        for dj in [-1, 1]:
            index = (j + dj - col) % col
            a[i][j] += ls[i][index]

for i in range(row):
    for j in range(col):
        print(a[i][j], end=' ')
    print()


# Из сайта
# c = []
# while True:
#     a = [i for i in input().split()]
#     if a == ['end']:
#         break
#     c.append(a)
# n, m = len(c), len(c[0])
# for i in range(n):
#     for j in range(m):
#         x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
#         print(x, end=' ')
#     print()