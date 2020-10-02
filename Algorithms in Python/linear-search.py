# Time Complexity - O(n)

def main():

    # array takes in space separated numbers from the user 
    array = list(map(int, input("Enter the numbers separated with space: ").strip().split(" ")))
    
    # search takes in the number ot be searched for
    search = int(input("Enter the element you want to search for: "))

    # Checking the if search is in array
    for i in range(len(arr)):
        if array[i] == search:
            print(f"Element {search} found at {i+1}")
        else:
            print("Element Not Found")


if __name__ == "__main__":
        main()