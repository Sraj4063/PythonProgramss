import  random
import math

def merge(arr,left,right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

def mergeSort(arr):
    if len(arr) > 1:
        mid = (len(arr))//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(arr,left,right)

n = eval(input("no.of elements to be sort"))
arr  = []
for i in range(0,n):
    arr.append(random.randint(1,1000))
print(arr)
mergeSort(arr)
print(arr)