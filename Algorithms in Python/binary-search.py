
# Time complexity : O(log n to the base 2s)

def main():

    # array takes in space separated numbers from the user
    array = list(
        map(int, input("Enter the numbers separated with space: ").strip().split(" ")))

    # search takes in the number ot be searched for
    search = int(input("Enter the element you want to search for: "))

    # Start and end indices of the input array
    start = 0
    end = len(array) - 1

    # Calling the binary search method
    output = binary_search(0, len(array)-1, array, search)

    if output == -1:
        print(f"{search} not found")
    else:
        print(f"{search} found at the position {output}")


# Recursive implementation of binary search
def binary_search(start, end, array, element):

    if start <= end:

        # Calculating the middle index
        mid = int((start+end)/2)

        # Checking if the middle element is greater or lesser or equal to the search element
        if(array[mid] > element):
            binary_search(start, mid-1, array, element)
        elif array[mid] < element:
            binary_search(mid+1, end, array, element)
        else:
            return mid
    else:
        return -1


if __name__ == "__main__":
    main()

# Python 3 program for recursive binary search. 
# Modifications needed for the older Python 2 are found in comments. 

# Returns index of x in arr if present, else -1 
def binary_search(arr, low, high, x): 

	# Check base case 
	if high >= low: 

		mid = (high + low) // 2

		# If element is present at the middle itself 
		if arr[mid] == x: 
			return mid 

		# If element is smaller than mid, then it can only 
		# be present in left subarray 
		elif arr[mid] > x: 
			return binary_search(arr, low, mid - 1, x) 

		# Else the element can only be present in right subarray 
		else: 
			return binary_search(arr, mid + 1, high, x) 

	else: 
		# Element is not present in the array 
		return -1

# Test array 
# creating an empty list 
arr = [] 

# number of elements as input 
n = int(input("Enter number of elements : ")) 

# iterating till the range 
for i in range(0, n): 
	ele = int(input()) 

	arr.append(ele) # adding the element 
	
print(arr) 

x =int(input("Enter element to be searched : ")) 

# Function call 
result = binary_search(arr, 0, len(arr)-1, x) 

if result != -1: 
	print("Element is present at index", str(result)) 
else: 
	print("Element is not present in array") 

