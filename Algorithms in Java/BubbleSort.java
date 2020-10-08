// Moves all greater value integers to the right and the lesser value integers to the left.
// Best case : Ω(n)
// Worst case : O(n^2)

import java.util.Scanner;

public class BubbleSort {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter array size.");
        int arraySize = input.nextInt();
        int[] items = new int[arraySize];

        System.out.println("Enter elements of the array.");
        for (int i = 0; i < arraySize; i++){
            items[i] = input.nextInt();
        }

        bubbleSort(items);

        System.out.println("Sorted elements of the array:");
        for (int i = 0; i < arraySize; i++){
            System.out.print(items[i] + " ");
        }
    }

    static void bubbleSort(int[] items) {
        int i, j, temp;
        boolean swapped = false;
        for (i = 0; i < items.length; i++){
            for (j = 0; j < (items.length - 1 - i); j++) {
                if (items[j] > items[j+1]) {
                    temp = items[j];
                    items[j] = items[j+1];
                    items[j+1] = temp;
                    swapped = true;
                }
            }
            if (swapped == false) {
                break;
            }
        }
    }
}