using System.Collections.Generic;
using System.Linq;
using System.Text;
using System;

namespace LinearSearch {
    class Program {
        public static void Main (string[] args) {
            int search_item;
            int pos = 0;

            List<int> list = new List<int>();

            Console.Write("How many numbers you want to enter? ");
            int n = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter the numbers\n");
            for (int i = 0; i < n; i++)
            {
                Console.Write("Number " + (i+1) + ": ");
                list.Add(int.Parse(Console.ReadLine()));
            }

            Console.Write ("Enter item to search : ");
            search_item = int.Parse (Console.ReadLine ());

            //Loop to search element in array.
            for (int i = 0; i < list.Count; i++) {
                if (search_item == list[i]) {
                    pos = i + 1;
                    break;
                }
            }

            if (pos == 0) {
                Console.WriteLine ("Item Not found in array");
            } else {
                Console.WriteLine ("Position of item in array: " + pos);
            }

        }
    }
}