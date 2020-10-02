def main():

    # array takes in space separated numbers from the user
    array = list(
        map(int, input("Enter the numbers separated with space: ").strip().split(" ")))

    # Calling the binary search method
    output = insertion_sort(array)
    print(f"The sorted array is: {output}")


def insertion_sort(array):

    for i in range(1, len(array)):

        value = array[i]

        hole = i-1

        while value < array[hole]:
            array[hole + 1] = array[hole]
            hole -= 1

        array[hole + 1] = value

    return array


if __name__ == "__main__":
    main()
