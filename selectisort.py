list = [1, -12,3,4,-4,3,2,-1,-8,.8]

for l in range(len(list)):
    mMin = l
    for m in range(l+1, len(list)):
        if list[m] < list[mMin]:
            mMin = m
    if mMin != l:
        list[l], list[mMin] = list[mMin], list[l]

print(list)