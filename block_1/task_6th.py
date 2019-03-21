num_pro = int(input())

if num_pro % 10 == 1 and num_pro % 100 != 11:
    print(str(num_pro) + " программист")
elif(num_pro % 10 == 2 or num_pro % 10 == 3 or num_pro % 10 == 4) and (num_pro % 100 != 12 and num_pro % 100 != 13 and num_pro % 100 != 14):
    print(str(num_pro) + " программиста")
else:
    print(str(num_pro) + " программистов")