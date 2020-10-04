# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:25:08 2020

@author: Aryan
"""

def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  

lst = [] 
  
n = int(input("Enter number of elements : ")) 
  
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 
  
bubbleSort(lst) 
  
print ("Sorted array is:") 
for i in range(len(lst)): 
    print ("%d" %lst[i] ,end="," ),  