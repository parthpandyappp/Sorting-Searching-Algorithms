import java.util.*;
import java.io.*;
class binarySearch
{
    public static void main(String args[])
    {
      int item=0, limit=0, beg=0, last=0, mid=0;
      int arr[]=new int[50];
      Scanner sc=new Scanner(System.in);
    
      System.out.println("Enter size of the array : -");
       limit=sc.nextInt();

    last = limit-1;
    System.out.println("Enter elements into array :- ");
    for(int i=0; i<limit; i++)
    {
        arr[i]=sc.nextInt();
    }

    System.out.println("Enter the element you want to search for : ");
    item=sc.nextInt();;
    while(beg<=last)
    {
        mid = (beg + last)/2;

        if(arr[mid] == item)
        {
            System.out.println("Search successful! Element "+item + " found at "+ (mid+1) + " position");
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
}
