// Program for selection-sort
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
	selectionsort(slice)
	fmt.Println("\nSorted array is: \n", slice, "\n")
}

func selectionsort(items []int) {
	var n = len(items)
	for i := 0; i < n; i++ {
		var minIdx = i
		for j := i; j < n; j++ {
			if items[j] < items[minIdx] {
				minIdx = j
			}
		}
		items[i], items[minIdx] = items[minIdx], items[i]
	}
}
