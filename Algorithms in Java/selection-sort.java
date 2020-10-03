import java.util.*;
import java.io.*;
class SelectionSort
{
    public static void main(String args[])
    {

    int item, limit=0, pos=0, small=0;
    int arr[]= new int[50];
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter size of array : ");
    limit=sc.nextInt();

    System.out.println("Enter elements of the array : ");
    for(int i=0; i<limit; i++)
    {
        arr[i]=sc.nextInt();
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

    System.out.println("Sorted form of array is : ");
    for(i=0; i<limit; i++)
    {
        System.out.print(arr[i] +" ");
    }
}
}
