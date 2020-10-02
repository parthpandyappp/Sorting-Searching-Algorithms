

def binary_search(array, x, low, high):

    if high >= low:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:                                       #left half
            return binary_search(array, x, low, mid-1)
        else:                                                      #right half
            return binary_search(array, x, mid + 1, high)
    else:
        return -1


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = int(input("Enter the element to search[0-9]: "))

pos = binary_search(array, x, 0, len(array)-1)

if pos != -1:
    print("Element is present at index " + str(pos))
else:
    print("Not found")
print(array)
