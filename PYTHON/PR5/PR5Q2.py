def sort_descnd(array):
    n= len(array)
    for i in range(n-1):
        for j in range(i+1,n):
            if array[i]<array[j]:
                array[i],array[j] = array[j],array[i]
    print(array)
    

array = list(map(int,input().split()))

print(array)
sort_descnd(array)