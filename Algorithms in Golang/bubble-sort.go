// Bubble Search
// Two sorted
// Increasing
// Decreasing

package main

import (
	"fmt"
)

func bubbleSortIncrease(list []int, size int) {
	swapped := true

	for swapped {
		swapped = false

		for i:= 1; i < size; i++ {
			if list[i-1] > list[i] {
				list[i], list[i-1] = list[i-1], list[i]
				swapped = true
			}
		}
	}

	fmt.Println("Sorted increasing order : ")
	fmt.Println(list)

}

func bubbleSortDecrease(list []int, size int) {
	swapped := true

	for swapped {
		swapped = false
		
		for i:= 1; i < size; i++ {
			if list[i-1] < list[i] {
				list[i], list[i-1] = list[i-1], list[i]
				swapped = true
			}
		}
	}

	fmt.Println("Sorted decreasing order : ")
	fmt.Println(list)
	
}

func main(){
	var size int
	fmt.Println("Enter the size of an array : ")
	fmt.Scan(&size)

	list := make([]int, size, 100)

	fmt.Println("Enter each element : ")
	for i := 0; i < size; i++{
		fmt.Scan(&list[i])
	}

	bubbleSortIncrease(list,size)
	bubbleSortDecrease(list,size)

}