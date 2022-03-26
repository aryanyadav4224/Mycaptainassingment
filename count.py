def most_frequent():
    s = "mississippi"
    d = {}
    for key in s:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    s = sorted(d.items(),key = lambda item : item[1], reverse = True)
    return s


print(most_frequent())