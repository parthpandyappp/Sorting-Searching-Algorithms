// Time complexity : O(log n to the base 2s)

#include <iostream>


int main()
{
    int item=0, arr[50], limit=0, beg=0, last=0, mid=0; 
    
    std::cout << "Enter size of the array : ";
    std::cin >> limit;

    last = limit-1;
    std::cout << "Enter elements into array : ";
    for(int i=0; i<limit; i++)
    {
        std::cin >> arr[i];
    }

    std::cout << "\nEnter the element you want to search for : ";
    std::cin >> item;
    while(beg<=last)
    {
        mid = (beg + last)/2;

        if(arr[mid] == item)
        {
            std::cout << "Search successful! Element " << item << " found at " << mid+1 << " position";
            break;
        }
        else if(item < arr[mid])
        {
            last = mid-1;
        }
        else
        {
            beg = mid+1;
        }
    }
    
}