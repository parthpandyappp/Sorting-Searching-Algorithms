//Insertion Sort
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
        
        Console.WriteLine("\nThe Array is :");
        for (int i = 0; i < array_size; i++)
        	Console.Write(array[i] + "\t");
        insertsort(array, array_size);
		
        Console.WriteLine("\nThe Sorted Array is :");
        for (int i = 0; i < array_size; i++)
        	Console.Write(array[i] + "\t"); 
    }        
    static void insertsort(int[] data, int n)
    {
    	int i, j;
        for (i = 1; i < n; i++)
        {
        	int item = data[i];
            int ins = 0;
            for (j = i - 1; j >= 0 && ins != 1; )
            {
            	if (item < data[j])
                {
                	data[j + 1] = data[j];
                    j--;
                    data[j + 1] = item;
                }
                else 
					ins = 1;
			}
        }
	}
}