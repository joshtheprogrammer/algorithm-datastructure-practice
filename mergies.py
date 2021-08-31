def mergesort(problem):
    if len(problem) > 1:

        m = len(problem)//2
        l, r = problem[:m], problem[m:]

        #divides all numbers
        mergesort(l)
        mergesort(r)

        left, right, k = 0,0,0

        #this is because it divides
        while left < len(l) and right < len(r):
            if l[left] < r[right]:
                problem[k]=l[left]
                left+=1
            else:
                problem[k] = r[right]
                right+=1
            k += 1

        while left < len(l):
            problem[k] = l[left]
            left += 1
            k += 1
        
        while right < len(r):
            problem[k]=r[right]
            right += 1
            k += 1
        


mergies = [3,1,3,2,3,39,8,.1,1010010]
mergesort(mergies)
print(mergies)


