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


lst = []
size = int(input("Enter size of the list: "))
for n in range(size):
    num = int(input("Enter Element: "))
    lst.append(num)
   
lst.sort()
x = int(input("Enter the element to search: "))

pos = binary_search(lst, x, 0, len(lst)-1)

if pos != -1:
    print("Element is present at index " + str(pos))
else:
    print("Not found")
print(lst)
