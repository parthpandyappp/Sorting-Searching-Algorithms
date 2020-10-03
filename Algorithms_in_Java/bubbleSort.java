//compare adjacent elements and move the larger element to the right
//this sorts the array such that the largest elemt in each itteration is moved to the right

package Algorithms_in_Java;

import java.util.Scanner;

public class bubbleSort {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int limit = 5; //default value
        System.out.println("Enter the size of the array");
        limit = sc.nextInt();
        int[] arr = new int[limit]; 
        System.out.println(arr.length);

        int i=0,j=0,temp;

        for(i=0;i<limit;i++){
            System.out.println("Enter the "+(i+1)+" number");
            arr[i] = sc.nextInt();
        }

        
        for(i=0;i<limit;i++){
            for(j=0;j<(limit-1)-i;j++){
                if(arr[j] > arr[j+1]){
                    temp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        System.out.println("Sorted array: ");
        for(i=0;i<limit;i++){
            System.out.println(arr[i]);
        }
        sc.close();
    }
}