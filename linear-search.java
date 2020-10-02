import java.util.*;
import java.io.*;
class linearSearch
{
public static void main(String args[])
{
    int item=0;
    int arr[]=new int[10];
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter 10 numbers to be inserted in the array : ");

    for(int i=0; i<10; i++)
    {
        arr[i]=sc.nextInt();
    }

    System.out.println("Your array : ");

    for(int i=0; i<10; i++)
    {
        System.out.println( arr[i] +" ");
    }

    System.out.println("Enter the element you want to search for : ");
     item=sc.nextInt();

    for(int i=0; i<10; i++)
    {
        if(item == arr[i])
        {
            System.out.println( "Element " + item + " found at " + (i+1) + " position.");
        }
    }
}
}
