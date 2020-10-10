import java.util.Scanner;

public class Main
{  
 public static void main(String args[])
 {
 Scanner sc = new Scanner(System.in);
 
         int i,n,pos;
 
 System.out.println("Enter the number of elements:") ;
 n = sc.nextInt();
 int[] a = new int[n];
 
     System.out.println("Enter the elements") ;
     for(i=0;i<n;i++)
     {
         a[i] = sc.nextInt();
     }
 
     
 System.out.println("Enter the position of the number which is to be deleted");
 pos = sc.nextInt();
    
 for(i=pos;i<n-1;i++)
     	{
         a[i]=a[i+1];
     }
     n=n-1;
     
 System.out.println("\nOn deleting new array we get is\n");
     for(i=0;i<n;i++) 
     {
         System.out.println("a["+i+"] = "+a[i]);
     }
 }
}