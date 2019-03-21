dna = str(input()).lower()
cg_count = 0
for i in 'cg':
    cg_count = cg_count + dna.count(i)

print(cg_count/len(dna)*100)