# Searching an element in a list/array in python 
# can be simply done using \'in\' operator 
# Example: 
# if x in arr: 
# print arr.index(x) 

# If you want to implement Linear Search in python 

# Linearly search x in arr[] 
# If x is present then return its location 
# else return -1 

def search(arr, x): 

	for i in range(len(arr)): 

		if arr[i] == x: 
			return i 

	return -1

# creating an empty list 
lst = [] 

# number of elemetns as input 
n = int(input("Enter number of elements : ")) 

# iterating till the range 
for i in range(0, n): 
	ele = int(input()) 

	lst.append(ele) # adding the element 
x = int(input("Enter element to be searched : ")) 	
print(lst) 

search(lst,x]
