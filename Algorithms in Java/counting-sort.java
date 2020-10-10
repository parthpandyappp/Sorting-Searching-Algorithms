import java.util.*; 
import java.util.Scanner;
  
class countingSort { 
  
    static void countSort(int[] arr,int n) 
    { 
        int max = Arrays.stream(arr).max().getAsInt(); 
        int min = Arrays.stream(arr).min().getAsInt(); 
        int range = max - min + 1; 
        int count[] = new int[range]; 
        int output[] = new int[n]; 
        for (int i = 0; i < n; i++) { 
            count[arr[i] - min]++; 
        } 
  
        for (int i = 1; i < count.length; i++) { 
            count[i] += count[i - 1]; 
        } 
  
        for (int i = n - 1; i >= 0; i--) { 
            output[count[arr[i] - min] - 1] = arr[i]; 
            count[arr[i] - min]--; 
        } 
  
        for (int i = 0; i < n; i++) { 
            arr[i] = output[i]; 
        } 
    } 
  
    static void printArray(int[] arr,int n) 
    { 
        System.out.print("Sorted Array: ");
        for (int i = 0; i < n; i++) { 
            System.out.print(arr[i] + " "); 
        } 
        System.out.println(""); 
    } 
    public static void main(String[] args) 
    { 
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of array: ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        System.out.print("Enter the elements of array: ");
        for (int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        } 
        countSort(arr,n); 
        printArray(arr,n); 
    } 
} 