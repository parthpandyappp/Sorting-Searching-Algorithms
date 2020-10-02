import random

def linear_search(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = []
size = int(input("Enter size of the list: "))
for n in range(size):
    num = int(input("Enter Element: "))
    array.append(num)
    
x = int(input("Enter the element to search: "))
n = len(array)
pos = linear_search(array, n, x)
if(pos == -1):
    print("Element not found")
else:
    print("Element found at index: ", pos)
print(array)
