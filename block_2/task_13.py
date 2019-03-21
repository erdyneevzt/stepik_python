a = [int(i) for i in input().split()]
x = int(input())

j = 0
for i in range(len(a)):
    if a[i] == x:
        print(i, end=' ')
        j = 1

if j == 0:
    print('Отсутствует')