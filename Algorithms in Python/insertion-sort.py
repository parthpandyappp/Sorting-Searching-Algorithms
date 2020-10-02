# Sorting function
def insertionSort(arr): 
    size = len(arr)
    for i in range(1, size): 
        key = arr[i] 
        j = i - 1
        while (j > -1) and (key < arr[j]): 
            arr[j + 1] = arr[j] 
            j = j - 1
        arr[j + 1] = key 
    
    return arr

n = int(input("Enter size : "))
arr = list()
print("Enter elements : ")
for i in range(0, n):
    element = int(input())
    arr.append(element)

arr = insertionSort(arr)
print("Sorted : ",arr)