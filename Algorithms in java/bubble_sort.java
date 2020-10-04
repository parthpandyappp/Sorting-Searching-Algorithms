
import java.util.Arrays;
import java.util.Scanner;

class Main {

  
  Scanner sc = new Scanner(System.in);

  
  void bubbleSort(int array[]) {
    int size = array.length;

    
    
    int sortOrder = sc.nextInt();

   
    for (int i = 0; i < size - 1; i++){
      
      for (int j = 0; j < size - i - 1; j++){

        
         
          
          if (array[j] > array[j + 1]) {

            
            int temp = array[j];
            array[j] = array[j + 1];
            array[j + 1] = temp;
          } 
        }
        
    }
       
  }

   public static void main(String args[]) {
    Scanner sc =new Scanner(System.in);
    System.out.println("Enter no. of elements:");
    int n=sc.nextInt();
    int[] data = new int[n];
    for(int k=0;k<n;k++)
    {   System.out.println("Enter the Element");
        data[k]=sc.nextInt();
    }
    
    Main c = new Main();

    
    c.bubbleSort(data);
    System.out.println("Sorted Array in Ascending Order:");

   
    System.out.println(Arrays.toString(data));
  }
}
