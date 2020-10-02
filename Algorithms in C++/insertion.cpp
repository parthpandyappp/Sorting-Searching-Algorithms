//Considering that given array is sorted. Now, the item to be inserted in this array must also be sorted. So, in this case the loop iterates over a check and it checks the item against all the elements in the array. Below points to be noted : 

// 1. If item is smaller then the first element of the array. Then loop iterates from limit to 0 in reverse order with appending one more block of the array in the existing and placing the item at '0'.

// 2. If item is equal to or greater than the current element in the array and also item to be less then the very next element, then the current position is returned and shifting iterates from limit to pos in reverse order.

// 3. The last case, when above none work this should obviously the last test case in "Insertion in Arrays". When iteration is equal to limit, i.e. item is greater than the last most element of the array then, the last position is returned and loop iterates from limit to limit, such that the element to be inserted in the sorted array is successfully appended to the last index.

#include <iostream>

int sort(int, int[], int);

int main()
{
    int item, arr[50], limit=0, pos=0;
    char ch='y';

    std::cout << "Enter size of array : ";
    std::cin >> limit;

    std::cout << "Enter elements of the array : ";
    for(int i=0; i<limit; i++)
    {
        std::cin >> arr[i];
    }

    while(ch=='y'|| ch=='Y')
    {
        if(limit>=50)
        {
            std::cout << "Overflow!!";
        }

        std::cout << "Enter the element to be inserted : ";
        std::cin >> item;

        int index;
        index = sort(limit, arr, item);
        //std::cout << "\nPosition from Sort is : " << index;
        for(int i=limit; i > index; i--)
        {
            arr[i] = arr[i-1];
        }

        arr[index] = item;
        limit += 1;

        std::cout << "Wanna insert more ? ('Y' for yes and 'N' for no)";
        std::cin >> ch;
    }

    std::cout << "\nArray now looks like : ";
    for(int i=0; i < limit; i++)
    {
        std::cout << arr[i] << " ";
    }
}

int sort(int limit, int arr[], int item)
{
    int i=0, pos=0;
    if(item < arr[0])
    {
        pos = 0;
    }

    else
    {
        for(i=0; i<limit-1; i++)
        {
            if(item>=arr[i] && item<arr[i+1])
            {
                pos = i+1;
            }

        }

    
        if(i==limit-1)
        {
            pos = limit;
        }
    }
    return pos;
}