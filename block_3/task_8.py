with open("dataset_3363_4.txt", "r", encoding='utf-8') as file:
    puples = file.read().split('\n')

math= 0
phy = 0
rus = 0
for i in range(len(puples)):
    marks = [int(i) for i in puples[i].split(';')[1:]]
    print(sum(marks)/3)
    math    += marks[0]
    phy     += marks[1]
    rus     += marks[2]

print(math/len(puples), phy/len(puples), rus/len(puples))



# st = [x.split(';') for x in open('fl.txt').readlines()]
# print(*[sum([int(y) for y in x[1:]])/3 for x in st], sep='\n')
# print(*[sum([int(y) for y in [st[x][z] for x in range(len(st))]])/len(st) for z in range(1,4)])