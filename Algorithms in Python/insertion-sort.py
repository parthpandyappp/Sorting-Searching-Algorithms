# Python program for implementation of Insertion Sort 

# Function to do insertion sort 
def insertionSort(arr): 

	# Traverse through 1 to len(arr) 
	for i in range(1, len(arr)): 

		key = arr[i] 

		# Move elements of arr[0..i-1], that are 
		# greater than key, to one position ahead 
		# of their current position 
		j = i-1
		while j >=0 and key < arr[j] : 
				arr[j+1] = arr[j] 
				j -= 1
		arr[j+1] = key 


# Driver code to test above 
# creating an empty list 
arr = [] 

# number of elements as input 
n = int(input("Enter number of elements : ")) 

# iterating till the range 
for i in range(0, n): 
	ele = int(input()) 

	arr.append(ele) # adding the element 
	
print(arr) 

insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
	print ("%d" %arr[i]) 
