//Time complexity is : O(n)

#include <iostream>


int main()
{
    int item=0, arr[10];

    std::cout << "Enter 10 numbers to be inserted in the array : \n";

    for(int i=0; i<10; i++)
    {
        std::cin >> arr[i];
    }

    std::cout << "Your array : \n";

    for(int i=0; i<10; i++)
    {
        std::cout  << arr[i] << " ";
    }

    std::cout << "\nEnter the element you want to search for : ";
    std::cin >> item;

    for(int i=0; i<10; i++)
    {
        if(item == arr[i])
        {
            std::cout << "Element " << item << " found at " << i+1 << " position.";
        }
    }
}