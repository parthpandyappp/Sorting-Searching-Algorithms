import java.util.Arrays;
import java.util.Scanner;

public class IterativeMergeSort {

    // Utility function to find minimum of two integers
    public static int min(int x, int y) {
        return (x < y) ? x : y;
    }

    /**
     * Java method to merge two sub-arrays of arr[] which are arr[l..m] and
     * arr[m+1..r]
     * 
     * @param int[] arr : array to be sorted
     * @param int   l : starting index
     * @param int   m : mid index
     * @param int   r : end index
     */
    public static void merge(int[] arr, int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;
        int[] L = new int[n1];
        int[] R = new int[n2];
        for (int i = 0; i < n1; i++) {
            L[i] = arr[l + i];
        }
        for (int j = 0; j < n2; j++) {
            R[j] = arr[m + 1 + j];
        }
        int i = 0, j = 0;
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    /**
     * Java method to sort array using mergeSort
     * 
     * @param int[] arr : array to be sorted
     * @param int   n : length of array
     */
    public static void mergeSort(int[] arr, int n) {
        int curr_size;
        int left_start;
        for (curr_size = 1; curr_size < (n - 1); curr_size = 2 * curr_size) {
            for (left_start = 0; left_start < (n - 1); left_start += 2 * curr_size) {
                int mid = min(left_start + curr_size - 1, n - 1);
                int right_end = min(left_start + 2 * curr_size - 1, n - 1);
                merge(arr, left_start, mid, right_end);
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
        mergeSort(arr, arr.length);
        System.out.println("Sorted array : " + Arrays.toString(arr));
        sc.close();
    }
}
