# Sorting function
def bubbleSort(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range (0, size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

n = int(input("Enter size : "))
arr = list()
print("Enter elements : ")
for i in range(0, n):
    element = int(input())
    arr.append(element)

arr = bubbleSort(arr)
print("Sorted : ",arr)
