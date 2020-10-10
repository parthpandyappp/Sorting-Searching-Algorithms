import java.util.Arrays;
import java.util.Scanner;

public class IterativeQuicksort {
    /**
     * Java method to partition array by placing elements lower than pivot to left
     * of pivot and those higher than pivot to the right
     * 
     * @param int[] arr : array to be sorted
     * @param int   low : starting index
     * @param int   high : ending index
     * @return index of pivot
     */
    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        arr[high] = arr[i + 1];
        arr[i + 1] = pivot;
        return i + 1;
    }

    /**
     * Java method to sort array using quicksort
     * 
     * @param int[] arr : array to be sorted
     * @param int   low : starting index
     * @param int   high : ending index
     */
    public static void quicksort(int[] arr, int low, int high) {
        int[] stack = new int[high - low + 1];
        int top = -1;
        stack[++top] = low;
        stack[++top] = high;
        while (top >= 0) {
            high = stack[top--];
            low = stack[top--];
            int p = partition(arr, low, high);
            if (p - 1 > low) {
                stack[++top] = low;
                stack[++top] = p - 1;
            }
            if (p + 1 < high) {
                stack[++top] = p + 1;
                stack[++top] = high;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter length of input array : ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        System.out.println("Enter elements of input array : ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println("Original array : " + Arrays.toString(arr));
        quicksort(arr, 0, arr.length - 1);
        System.out.println("Sorted array : " + Arrays.toString(arr));
        sc.close();
    }

}
