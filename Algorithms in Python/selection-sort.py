# Sorting function
def selectionSort(arr):
    size = len(arr)
    for i in range(size - 1):
        minIndex = i
        for j in range (i+1, size):
            if arr[j] < arr[minIndex]:
                minIndex = j

        if minIndex != i:
            arr[minIndex], arr[i] = arr[i], arr[minIndex]
    
    return arr

n = int(input("Enter size : "))
arr = list()
print("Enter elements : ")
for i in range(0, n):
    element = int(input())
    arr.append(element)

arr = selectionSort(arr)
print("Sorted : ",arr)