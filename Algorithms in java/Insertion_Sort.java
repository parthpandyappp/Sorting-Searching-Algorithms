import java.util.Scanner;

public class InsertionSort {

        /Function to sort array using insertion sort/
        void sort(int arr[])
        {
            int n = arr.length;
            for (int i = 1; i < n; ++i) {
                int key = arr[i];
                int j = i - 1;


        static void printArray(int arr[])
        {
            int n = arr.length;
            for (int i = 0; i < n; ++i)
                System.out.print(arr[i] + " ");

            System.out.println();
        }

        public static void main(String args[])
        {
            int n;
            Scanner s = new Scanner(System.in);
            System.out.print("Enter no. of elements you want in array:");
            n = s.nextInt();

            int arr[] = new int[n];
            System.out.println("Enter all the elements:");
            for(int i = 0; i < n; i++)
            {
                arr[i] = s.nextInt();
            }


            InsertionSort ob = new InsertionSort();
            ob.sort(arr);

            printArray(arr);
        }
    }
