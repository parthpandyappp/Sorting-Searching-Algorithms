//Selection Sort
using System;
public class Program
{
    public static void Main(string[] args)
    {
        int array_size = Convert.ToInt32(Console.ReadLine());
        int[] array = new int[array_size];
		for(int i=0; i < array_size; i++)  
    	{  
	    	Console.Write("element - {0} : ",i);
	    	array[i] = Convert.ToInt32(Console.ReadLine());  		
    	} 
        Console.WriteLine("\nThe Array Before Selection Sort is: ");
        for (int i = 0; i < array_size; i++)
        {
            Console.Write(array[i] + "\t");
        }
        int tmp, min;
 
        for (int j = 0; j < array_size - 1; j++)
        {
            min = j;
 
            for (int k = j + 1; k < array_size; k++)
            {
                if (array[k] < array[min])
                    min = k;
            }
 
            tmp = array[min];
            array[min] = array[j];
            array[j] = tmp;
        }
 
        Console.WriteLine("\nThe Array After Selection Sort is: ");
        for (int i = 0; i < array_size; i++)
        {
            Console.Write(array[i] + "\t");
        }
    }
}