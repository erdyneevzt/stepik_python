num_1 = float(input())
num_2 = float(input())
oper  = str(input())

if oper == "+":
    print(num_1+num_2)
elif oper == "-":
    print(num_1 - num_2)
elif oper == "/":
    if num_2 == 0:
        print("Деление на 0!")
    else:
        print(num_1/num_2)
elif oper == "*":
    print(num_1 * num_2)
elif oper == "mod":
    if num_2 == 0:
        print("Деление на 0!")
    else:
        print(num_1 % num_2)
elif oper == "pow":
    print(num_1**num_2)
elif oper == "div":
    if num_2 == 0:
        print("Деление на 0!")
    else:
        print(num_1//num_2)
