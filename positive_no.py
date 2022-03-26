list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
print ('all positive num. in list 1')
for int in list1:
    if int < 0:
        continue;
    print(int)
print ('all positive num. in list 2')
for int in list2:
    if int < 0:
        continue;
    print(int)