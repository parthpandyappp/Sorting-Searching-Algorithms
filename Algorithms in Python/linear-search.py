# Time Complexity - O(n)

def main():

    # array takes in space separated numbers from the user 
    array = list(map(int, input("Enter the numbers separated with space: ").strip().split(" ")))
    
    # search takes in the number ot be searched for
    search = int(input("Enter the element you want to search for: "))

    flag = 0
    # Checking the if search is in array
    for i in range(len(array)):
        if array[i] == search:
            print(f"Element {search} found at {i+1}")
            flag = 1
            
    if flag == 0:
        print("Element not found")   


if __name__ == "__main__":
        main()