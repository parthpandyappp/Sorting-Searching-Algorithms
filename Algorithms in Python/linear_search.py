import random

def linear_search(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = random.sample(range(0, 9), 5)
x = int(input("Enter the element to search[0-9]: "))
n = len(array)
pos = linear_search(array, n, x)
if(pos == -1):
    print("Element not found")
else:
    print("Element found at index: ", pos)
print(array)
