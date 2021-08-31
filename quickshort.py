list = [2, 7, 1, 7, 3, 7, 8, 4, 8]

def QuickSort(array, left, right):
    if left < right:
        pivot = array[(left+right)//2]
        index = partition(array, left, right, pivot)
        QuickSort(array, left, index-1)
        QuickSort(array, index, right)

def partition(array, left, right, pivot):
    while left <= right:
        while array[left] < pivot:
            left+=1
        while array[right] > pivot:
            right-=1
        
        if left<=right:
            array[left], array[right]=array[right], array[left]
            left+=1
            right-=1
    return left

QuickSort(list, 0, len(list)-1)

print(list)