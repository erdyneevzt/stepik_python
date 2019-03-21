lst = [1, 4, 3, 5, 6, 7]
# lst.remove(lst[5])
# print(lst)

def modify_list(lst):
    i = 0
    index = 0
    leng = len(lst)
    while i < leng:
        if lst[index] % 2 == 1:
            del lst[index]
            i += 1
        else:
            lst[index] = lst[index] // 2
            index += 1
            i += 1

modify_list(lst)
print(lst)

# def modify_list(l):
#     l[:] = [i//2 for i in l if not i % 2]