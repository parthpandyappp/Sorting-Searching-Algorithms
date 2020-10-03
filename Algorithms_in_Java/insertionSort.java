//select a number and comapare it with all numbers before it in the array and then insert it into the right position

package Algorithms_in_Java;

import java.util.Scanner;

public class insertionSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int limit = 5; //default value
        System.out.println("Enter the size of the array: ");
        limit = sc.nextInt();
        int[] arr = new int[limit];

        int i=0,j=0,temp;
        for(i=0;i<limit;i++){
            System.out.println("Enter the "+(i+1)+" number");
            arr[i] = sc.nextInt();
        }

        for(i=1;i<limit;i++){
            j=i-1;
            while(arr[j]>arr[i] && j>=0){
                j--;
                if(j<0){
                    break;
                }
            }
            j++;
            int k=i-1;
            temp = arr[i];
            for(k=i-1;k>=j;k--){
                arr[k+1]=arr[k];
            }
            arr[j] = temp;
        }

        System.out.println("Sorted array : ");
        for(i=0;i<limit;i++){
            System.out.println(arr[i]);
        }
    }
}
