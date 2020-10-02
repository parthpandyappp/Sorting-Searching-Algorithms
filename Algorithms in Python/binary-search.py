# For binary-search arr must be sorted

# Searching function
def binarySearch(arr, low, high, key):
    while(low <= high):
        mid = low + ((high- low) // 2)
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    # In case of element not found
    return -1


n = int(input("Enter size : "))
arr = list()
print("Enter elements : ")
for i in range(0, n):
    element = int(input())
    arr.append(element)

# Searching Element
key = int(input("Enter your key element : "))

# Function call to Searching function
result = binarySearch(arr, 0, n - 1, key)

if(result == -1):
    print("Element not found")
else:
    print("Element found at index : ", result)


