# Searching function
def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print("Element found at index : ", i)
            return
    print("Element Not found ..")

n = int(input("Enter size : "))
arr = list()
print("Enter elements : ")
for i in range(0, n):
    element = int(input())
    arr.append(element)

# Searching Element
key = int(input("Enter your key element : "))

# Function call to Searching function
linearSearch(arr, key)