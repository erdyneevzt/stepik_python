ls = [i.lower() for i in input().split()]

s = {}
for i in range(len(ls)):
    if ls[i] not in s:
        s[ls[i]] = 1
    else:
        s[ls[i]] += 1

for key, value in s.items():
    print(key,value)


# s = input().lower().split()
# for i in set(s):
#     print(i, s.count(i))