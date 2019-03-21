text    = open('dataset_3363_3.txt')
seq     = text.read().strip().lower().split()

s = {}
for i in set(seq):
    s[i] = seq.count(i)

i = 0
ans = ''
for key in s.keys():
    if s[key] > i:
        ans = key
        i   = s[key]
    elif s[key] == i:
        if key < ans:
            ans = key

print(ans, i)

