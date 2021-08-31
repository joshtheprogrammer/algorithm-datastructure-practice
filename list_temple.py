list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for l in range(0, len(list)):
    lol = []
    lol2 = []
    for n in range(0, l+1):
        lol.append(list[n])
    for n2 in range(len(list)-1-l, len(list)):
        lol2.append(list[len(list)-1-n2])
    print(lol2,lol)      

for l in range(0, len(list)):
    lol3 = []
    lol4 = []
    for n3 in range(0, len(list)-l):
        lol3.append(list[n3])
    for n4 in range(l, len(list)):
        lol4.append(list[len(list)-1-n4])
    print(lol4,lol3)