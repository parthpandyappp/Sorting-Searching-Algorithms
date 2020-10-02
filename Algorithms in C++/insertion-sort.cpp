//a trickiest sorting algorithm but better according to me, simply iterates over all the elements of a given array to be sorted. Considers every 'i' th element in every parse as temp and sets j to i-1 to compare the current element from the past ones. Under the for loop, a while loop is placed which aims to iterate over the elements until a condition (Till the time when the elements are out of order) and in every parse of the while loop it decrements j to traverse back to the past elements and check them against the temp element. Finally, the temp element is placed at the appropriate position i.e where the while loop terminated lastly.

//Best case : Ω(n) 
//Worst case : O(n^2)
#include <iostream>

int main()
{
    int arr[50], limit=0, item=0;

    std::cout << "Enter size of the array : ";
    std::cin >> limit;

    std::cout << "Enter array elements : ";
    for(int i=0; i<limit; i++)
    {
        std::cin >> arr[i];
    }

    int temp, j;

    for(int i=0; i<limit; i++)
    {
        temp = arr[i];
        j = i-1;

        while(temp < arr[j])
        {
            arr[j+1] = arr[j];
            j--;
        }

        arr[j+1] = temp;
        std::cout << "\nArray after pass -" << i << "- : " ;
        for(int k=0; k<limit; k++)
        {
            std::cout << arr[k] << " ";
        }
    }

    std::cout << "\n\nFinal Sorted form of array is : ";
    for(int i=0; i<limit; i++)
    {
        std::cout << arr[i] << " ";
    }

}