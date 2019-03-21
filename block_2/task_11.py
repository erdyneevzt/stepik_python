ls = []
summ = 1
while summ != 0:
    ls.append(int(input()))
    summ = sum(ls)

sum_q = 0
for i in range(len(ls)):
    sum_q += ls[i]**2
print(sum_q)


# Решение из сайта
# s, d = 0, 0
# while True:
#     a = int(input())
#     s += a
#     d += a*a
#     if s == 0:
#         break
# print(d)

