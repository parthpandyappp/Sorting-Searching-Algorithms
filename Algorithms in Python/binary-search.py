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
