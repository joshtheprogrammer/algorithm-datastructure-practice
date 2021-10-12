list = [1, 2, 31,4 ,5, 7,0.1]

for i in range(len(list)-1):
    for j in range(0, len(list)-1-i):
        # (i=0) 1 2 (#31) <-> [=4 =5 =7 =0.1]
        if list[j] > list[j+1]:
           list[j], list[j+1] = list[j+1], list[j]
print(list)