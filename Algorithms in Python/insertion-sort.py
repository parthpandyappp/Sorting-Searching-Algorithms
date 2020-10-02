# a trickiest sorting algorithm but better according to me, simply iterates over all the elements of a given array to be sorted. Considers every 'i' th element in every parse as temp and sets j to i-1 to compare the current element from the past ones. Under the for loop, a while loop is placed which aims to iterate over the elements until a condition (Till the time when the elements are out of order) and in every parse of the while loop it decrements j to traverse back to the past elements and check them against the temp element. Finally, the temp element is placed at the appropriate position i.e where the while loop terminated lastly.

# Best case : Ω(n)
# Worst case : O(n^2)
def main():

    # array takes in space separated numbers from the user
    array = list(
        map(int, input("Enter the numbers separated with space: ").strip().split(" ")))

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
