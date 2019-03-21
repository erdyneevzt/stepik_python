a =[int(i) for i in input().split()]
b = []
for i in range(len(a)):
    if (len(a) == 1):
        b = a
    elif (i == (len(a)-1)):
        b.append(a[i-1] + a[0])
    else:
        b.append(a[i-1] + a[i+1])

for j in range(len(b)):
    print(b[j], end=' ')


# Оптимальное решение без обособления последнего варианта
# a=[int(i) for i in input().split()]
# if len(a)>1:
#     for i in range(len(a)):
#         print(a[i-1]+a[i+1-len(a)], end=' ')
# else:
#     print(a[0], end=' ')