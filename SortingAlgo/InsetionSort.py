n  = eval(input("no of elements you want ot insert"))
arr = []
a = 0
while a < n:
    arr.append(int(input("element = ")))
    a += 1
print(arr)
def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
print("Before sorring the array is",arr)
insertion(arr)
print("After sorting the arrray is ",arr)
