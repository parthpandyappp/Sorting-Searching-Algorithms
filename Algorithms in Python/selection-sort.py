def main():

    # array takes in space separated numbers from the user
    array = list(
        map(int, input("Enter the numbers separated with space: ").strip().split(" ")))

    # Calling the binary search method
    output = selection_sort(array)
    print(f"The sorted array is: {output}")


def selection_sort(array):

    for i in range(len(array)):

        start = i
        for j in range(i+1, len(array)):
            if array[start] > array[j]:
                start = j
        array[i], array[start] = array[start], array[i] 
    
    return array

if __name__ == "__main__":
    main()
