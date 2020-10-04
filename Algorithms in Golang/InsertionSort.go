//Program for insertion sort

package main

import (
	"fmt"
)

func main() {

	length := 0
	fmt.Println("Enter the number of inputs: ")
	fmt.Scanln(&length)

	fmt.Println("Enter the inputs: ")

	slice := make([]int, length)
	for i := 0; i < length; i++ {
		fmt.Scanln(&slice[i])
	}

	fmt.Println("\nUnSorted array is: \n\n", slice)
	fmt.Println("\nUnSorted array is: \n\n", slice)
	insertionsort(slice)
	fmt.Println("\nSorted array is: \n", slice, "\n")
}

func insertionsort(items []int) {
	var n = len(items)
	for i := 1; i < n; i++ {
		j := i
		for j > 0 {
			if items[j-1] > items[j] {
				items[j-1], items[j] = items[j], items[j-1]
			}
			j = j - 1
		}
	}
}
