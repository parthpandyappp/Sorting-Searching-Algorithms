def main():

    # array takes in space separated numbers from the user
    array = list(
        map(int, input("Enter the numbers separated with space: ").strip().split(" ")))

    del_element = int(input("Enter the element to be deleted: "))

    index = search(array,del_element)

    if index == -1:
        print(f"{del_element} not present")
        exit()
    # Calling the binary search method
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
