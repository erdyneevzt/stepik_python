n = int(input())
i = 1
k = 1
if n == 1:
    print(n)
else:
    while i < n:
        for j in range(k):
            print(k, end=' ')
            i += 1
            if i == n and j != k-1:
                print(k, end=' ')
                break
            elif i == n and j == k-1:
                print(k+1, end=' ')
        k += 1

# n = int(input())
# a = []
# i = 0
# while len(a) < n:
#     a += [i] * i
#     i += 1
# print(*a[:n])


# n = int(input())
# count = 0
# curr = 1
# for i in range(n):
#     print(curr, end=' ')
#     count += 1
#     if count == curr:
#         curr += 1
#         count = 0