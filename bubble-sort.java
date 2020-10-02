import java.util.*;
import java.io.*;
class bubbleSort
{
public static void main(String args[])
{
    int item, limit=0, pos=0, small=0;
    int arr[]=new int[50];
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter size of array : ");
    limit=sc.nextInt();
    System.out.println("Enter elements of the array : ");
    for(int i=0; i<limit; i++)
    {
        arr[i]=sc.nextInt();
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

    System.out.println("Array after sorting with Bubble Sort : ");
    for(i =0; i<limit; i++)
    {
        System.out.print(arr[i] +" ");
    }
   
}
}
