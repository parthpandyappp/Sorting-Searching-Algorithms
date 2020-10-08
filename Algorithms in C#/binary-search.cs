using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace BinarySearch {
    class Program {
        public static void Main () {
            int search_item = 0;
            int pos = 0;

            int LOW = 0;
            int HIGH = 0;
            int MID = 0;

            //Read numbers into array
            List<int> list = new List<int> ();

            Console.Write ("How many numbers you want to enter? ");
            int n = int.Parse (Console.ReadLine ());
            Console.WriteLine ("Enter the numbers\n");
            for (int i = 0; i < n; i++) {
                Console.Write ("Number " + (i + 1) + ": ");
                list.Add (int.Parse (Console.ReadLine ()));
            }
            Console.Write ("Enter item to search : ");
            search_item = int.Parse (Console.ReadLine ());

            HIGH = list.Count - 1;
            MID = (LOW + HIGH) / 2;

            //Loop to search element in array.
            while (LOW <= HIGH) {
                if (search_item < list[MID]) {
                    HIGH = MID - 1;
                    MID = (LOW + HIGH) / 2;
                } else if (search_item > list[MID]) {
                    LOW = MID + 1;
                    MID = (LOW + HIGH) / 2;
                } else if (search_item == list[MID]) {
                    pos = MID + 1;
                    break;
                }
            }

            if (pos == 0) {
                Console.WriteLine ("Item Not found in array");
            } else {
                Console.WriteLine ("Position of " + search_item + " in list: " + pos);
            }

        }
    }
}