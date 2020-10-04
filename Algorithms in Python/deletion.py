# Linearly searches for the element to be deleted, if in case find the position in the array that is temprarily set as '0' and after that loop iterates the array from the pos to limit, and shifts all to the appropriate side and lastly, it just deletes the last block of the array.
def main():

    # array takes in space separated numbers from the user
    array = list(
        map(int, input("Enter the numbers separated with space: ").strip().split(" ")))

    del_element = int(input("Enter the element to be deleted: "))

    index = search(array,del_element)

    if index == -1:
        print(f"{del_element} not present")
        exit()

    output = deletion(array,index)
    print(f"The sorted array is: {output}")


def deletion(array, index):

    array[index] = ""

    for i in reversed(range(index)):

        array[i+1] = array[i]
        print(array)

    return array[1:]

def search(array, element):
    
    flag = 0
    
    for i in range(len(array)):
        if array[i] == element:
            return i
    if flag == 0:
        return -1


if __name__ == "__main__":
    main()
