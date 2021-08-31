list = [1231, 123,4,5,6,-.1,-31,4,-39123]

for l in range(1, len(list)):
    key = list[l]
    m = l - 1

    while m >= 0 and key < list[m]:
        list[m+1] = list[m]
        m -= 1
    list[m+1] = key
    
print(list)
