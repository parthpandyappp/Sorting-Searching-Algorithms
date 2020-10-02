//Finds the smallest of all in the given array, every time the loop iterates. Considers a particular element of an array as small, and iterates a check with other elements in the array. In case it founds the comparision of array out of order, the elements are swapped.

// Time complexity analysis
//Best case : Ω(n^2)
//Worst case : O(n^2)

#include <iostream>

int main()
{
    int item, arr[50], limit=0, pos=0, small=0;

    std::cout << "Enter size of array : ";
    std::cin >> limit;

    std::cout << "Enter elements of the array : ";
    for(int i=0; i<limit; i++)
    {
        std::cin >> arr[i];
    }

    small = arr[0];
    int i=0, j=0;
    for(i=0; i<limit-1; i++)
    {
        small = arr[i];
        pos =i;
        for(j=i+1; j<limit; j++)
        {
            if(arr[j]<small)
            {
                small = arr[j];
                pos = j;
            }
        }

        int temp = arr[i];
        arr[i] = small;
        arr[pos] = temp; 

    }

    std::cout << "Sorted form of array is : ";
    for(i=0; i<limit; i++)
    {
        std::cout << arr[i] << " ";
    }
}