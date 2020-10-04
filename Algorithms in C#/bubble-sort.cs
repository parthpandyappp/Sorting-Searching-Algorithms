using System;
using System.Collections.Generic;

namespace BubbleSort
{
    public class Program
    {
        public static void Main(string[] args)
        {
            List<int> list = new List<int>();

            Console.Write("How many numbers you want to enter? ");
            int n = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter a numbers\n");
            for (int i = 0; i < n; i++)
            {
                Console.Write("Number " + (i+1) + ": ");
                list.Add(int.Parse(Console.ReadLine()));
            }

            Console.WriteLine("\nBefore sorting: ");
            foreach (var number in list)
            {
                Console.Write(number + " ");
            }
            BubbleSort(list);

            Console.WriteLine("\nAfter sorting: ");
            foreach (var number in list)
            {
                Console.Write(number + " ");
            }
        }

        public static void BubbleSort(List<int> list)
        {
            for (int i = 0; i < list.Count; i++)
            {
                for (int j = 1; j < list.Count - i; j++)
                {
                    if (list[j - 1] > list[j])
                    {
                        var temp = list[j - 1];
                        list[j - 1] = list[j];
                        list[j] = temp;
                    }
                }
            }
        }
    }
}
