//Aims to push all heavy elements in the right side and lighier to the extreme left.
//Best case : Ω(n)
//Worst case : O(n^2)

#include <iostream>

int main()
{
    int item, arr[50], limit=0, pos=0, small=0;

    std::cout << "Enter size of array : ";
    std::cin >> limit;

    std::cout << "\nEnter elements of the array : ";
    for(int i=0; i<limit; i++)
    {
        std::cin >> arr[i];
    }

    int i=0, j=0;
    for(i=0; i<limit; i++)
    {
        for(j=0; j<(limit-1)-i; j++)
        {
            if(arr[j]>arr[j+1])
            {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp; 
            }
        }
    }

    std::cout << "\nArray after sorting with Bubble Sort : ";
    for(i =0; i<limit; i++)
    {
        std::cout << arr[i] <<" ";
    }
    std::cout << "\n";
}