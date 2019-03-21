text    = open('dataset_3363_2.txt')
seq     = text.read().strip()
print(seq)

ls = len(seq)

tmpOut  =''
num     ='0'
char    =''

for i in range(ls):
    if seq[i].isalpha():
        tmpOut += char*int(num)
        char    = seq[i]
        num   = '0'
    else:
        num += seq[i]

tmpOut += char*int(num)


w = open('answer.txt', 'w')
w.write(tmpOut)

w.close()
text.close()


# with open('dataset_3363_2.txt', 'r') as f:
#     s = f.readline().strip()
# i = 0
# while i < len(s):
#     j = i + 1
#     while j < len(s) and s[j].isdigit():
#         j += 1
#     print(s[i] * int(s[i+1:j]), end='')
#     i = j
