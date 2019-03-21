lt = int(input())

f = lt % 10
s = (lt % 100)          // 10
t = (lt % 1000)         // 100
fo = (lt % 10000)       // 1000
fi = (lt % 100000)      // 10000
si  = (lt % 1000000)    // 100000

if ((f + s + t) - (fo + fi + si)) == 0:
    print("Счастливый")
else:
    print("Обычный")
