d = {}


def update_dictionary(d, key , value):
    if key in d:
        d[key].append(value)
    elif key not in d:
        if 2*key not in d:
            d[2*key] = [value]
        else:
            d[2*key].append(value)

update_dictionary(d,1,-1)
print(d)
update_dictionary(d,2,-2)
print(d)
update_dictionary(d,1,-3)
print(d)

# def update_dictionary(d, key, value):
#     key += key * (key not in d)
#     d[key] = d.get(key, []) + [value]