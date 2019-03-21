# slov = set()
# for i in range(int(input())):
#     slov.add(str(input().lower()))
#
# all_lines = []
# for i in range(int(input())):
#     all_lines[:] += str(input()).lower().split()
#
# repeats = []
# for i in all_lines:
#     if (i not in slov) and (i not in repeats):
#          print(i)
#          repeats.append(i)


dic = {input().lower() for i in range(int(input()))}

wrd = set()
for w in range(int(input())):
    wrd |= {i.lower() for i in input().split()}

print(*wrd.difference(dic), sep="\n")