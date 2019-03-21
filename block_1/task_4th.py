forma = str(input())

if forma == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p_half = (a + b + c) / 2
    s_triangle = (p_half * (p_half - a) * (p_half - b) * (p_half - c)) ** 0.5
    print(s_triangle)
elif forma == "прямоугольник":
    a = int(input())
    b = int(input())
    print(float(a*b))
elif forma == "круг":
    r = int(input())
    print(3.14*(r**2))
