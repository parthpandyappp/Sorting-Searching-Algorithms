
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

# Finds the smallest of all in the given array, every time the loop iterates. Considers a particular element of an array as small, and iterates a check with other elements in the array. In case it founds the comparision of array out of order, the elements are swapped

# Time complexity analysis
# Best case : Ω(n^2)
# Worst case : O(n^2)


def main():

    # array takes in space separated numbers from the user
    array = list(
        map(int, input("Enter the numbers separated with space: ").strip().split(" ")))

    output = selection_sort(array)
    print(f"The sorted array is: {output}")


def selection_sort(array):

    for i in range(len(array)):

        start = i
        for j in range(i+1, len(array)):
            if array[start] > array[j]:
                start = j
        array[i], array[start] = array[start], array[i]

    return array


if __name__ == "__main__":
    main()

