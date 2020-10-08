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