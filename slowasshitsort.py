#triangle sort?

list = [1, 0.1, 31,4 ,5, 7,0.1]

for i in range(len(list)):
    for j in range(len(list)):
        # (i=0, j=*) (1) <-> [0.1] 31 4 5 7 0.1
        # (i=1, j=*) 1 (0.1) 31 4 5 7 0.1
        # (i=2, j=0) [1] 0.1 <-> (31) 4 5 7 0.1
        # (i=2, j=1) 31 [0.1] <-> (1) 4 5 7 0.1
        if list[i] > list[j]:
            list[j], list[i] = list[i], list[j]
    print(list)