x = float(input())

def f(x):
    if x <= -2:
        a = 1 - (x+2)**2
        return a
    elif x > -2 and x <= 2:
        a = -x/2
        return a
    elif x >2:
        a = (x-2)**2 + 1
        return a

print(f(4.5))
