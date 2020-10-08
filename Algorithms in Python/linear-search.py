#linear-Search with menu

arr = []
flag = 1

def menu():
    print("\nWelcome To Linear Search Algorithm.\nSelect Operation To Perform\n")
    print("1 - Add values to array\n2 - Show array")
    print("3 - Search a value from array\n4 - Remove value from array\n5 - Reset array\n6 - Exit")
    perform = int(input("Enter index no. to perform specific operation: "))
    operations(perform)

def add_values():
    global arr
    #Adding values to array
    times = int(input("\nEnter no. of values to add: "))
    vals = [ int(input("Enter val "+str(i+1)+": " )) for i in range(times)]
    arr = arr + vals
def show_array():
    global arr
    #show values inside array 
    tmp = [i for i in arr]
    print(tmp)
    del tmp
def search_array():
    global arr
    #Can search multiple values from array
    srch_vals = input("\nEnter value to search | Enter multiple values to search with a space: ")
    tmp = [ print(i,"is present at index:",arr.index(int(i))) if int(i) in arr else print(i,"not present in array") for i in srch_vals.split() ]
    del tmp ,srch_vals
def remove_vals():
    global arr
    rmv_vals = input("Enter value to remove | Enter multiple values to remove with a space (Note: Duplicate will also be removed)\nvalue(s): ")
    tmp = [print(str(arr.remove(int(i))).replace('None',i),"is removed successfully") if int(i) in arr else print(i,"not found in array") for i in rmv_vals.split()]
    del tmp ,rmv_vals
def reset():
    global arr
    arr = []
    print("Array reset successfully")
def operations(id):
    global flag
    if id == 1:add_values()
    elif id == 2:show_array()
    elif id == 3:search_array()
    elif id == 4:remove_vals()
    elif id == 5:reset()
    elif id == 6:flag = 0
    else:print("Selected index is out of menu")

while True:
    menu()
    if not flag:
        print("Exiting the program!")
        break

#Previous Code
'''
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
    print("Element found at index: ", pos+1)
print(array)

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

search(lst,x)
'''