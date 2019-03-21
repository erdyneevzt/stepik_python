n = int(input())

s = {}
for i in range(n):
    x = int(input())
    if x in s:
        print(s[x])
    else:
        s[x] = f(x)
        print(f(x))


# a=[int(input()) for i in range(int(input()))]
# b={x:f(x) for x in set(a)}
# for i in a:
#     print(b[i])