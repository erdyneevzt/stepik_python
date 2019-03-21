a = int(input())
b = int(input())
c = int(input())

p_half = (a+b+c)/2
s_triangle = (p_half*(p_half-a)*(p_half-b)*(p_half-c))**0.5
print(s_triangle)