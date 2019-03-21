n = int(input())

mtx = [[0 for j in range(n)] for i in range(n)]

r, k = 0, 0
# 1 - Направление вправо
# 2 - Направление вниз
# 3 - Направление влево
# 4 - Направление вверх
dir = 1
row = n
col = n
for i in range(n**2):
    if dir == 1 and k != col-1:
        mtx[r][k] = i+1
        k += 1
    elif k == col-1 and r != row-1:
        dir = 2
        mtx[r][k] = i+1
        r += 1
    elif r == row-1 and k !=0:
        dir = 3
        mtx[r][k] = i+1
        k += -1
    elif k == 0 and r != 0:
        dir = 4
        mtx[r][k] = i+1
        r += -1


