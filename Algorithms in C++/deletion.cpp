//Linearly searches for the element to be deleted, if in case find the position in the array that is temprarily set as '0' and after that loop iterates the array from the pos to limit, and shifts all to the appropriate side and lastly, it just deletes the last block of the array.

#include <iostream>

int search(int, int[], int);

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
        if(limit==0 || limit>=50)
        {
            std::cout << "Not accepted!";
        }

        std::cout << "Enter the element to be deleted from the array : ";
        std::cin >> item;

        int index; 
        index = search(item, arr, limit); 

        if(index != -1)
        {
            std::cout << "\nItem found at " << index+1 << " now deleting ..."; 
            arr[index] = 0;
        }

        for(int i=index; i < limit; i++)
        {
            arr[i] = arr[i+1];
        }

        limit -= 1;

        std::cout << "\nWant to delete more ?";
        std::cin >> ch;

    }

    std::cout << "\nArray now looks like : ";
    for(int i=0; i<limit; i++)
    {
        std::cout << arr[i] << " ";
    }
}

int search(int item, int arr[], int limit)
{
    for(int i=0; i<limit; i++)
    {
        if(arr[i] == item)
        {
            return i;
        }
    }
    return -1;
}