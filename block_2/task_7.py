dna = str(input())

count = 1
for i in range(len(dna)):
    if len(dna) == 1:
        print(dna[i]+str(1))
    elif i+1 == len(dna)-1 and dna[i+1] == dna[i]:
        print(dna[i] + str(count+1), end='')
        break
    elif i+1 == len(dna)-1 and dna[i+1] != dna[i]:
        print(dna[i]+str(count)+dna[i+1]+str(1), end='')
        break
    elif dna[i+1] == dna[i]:
        count += 1
    else:
        print(dna[i]+str(count), end='')
        count = 1

# Альтернатива из сайта
genome = input()+' '
s = 0
n=genome[0]
for i in genome:
    if n!=i:
        print(n + str(s), end = '')
        s=0
        n=i
    s+=1