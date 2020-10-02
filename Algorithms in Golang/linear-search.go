// Linear Search
// Based on .cpp reference
// Array size is 10

package main

import (
	"fmt"
)

// Linear Search Function
func linearSearch(list [10]int, find int){
	for i := 0; i < 10; i++ {
		if list[i] == find {
			fmt.Println("Element found at position ", i+1)
			return
		}
  }

		fmt.Println("Element not found")
		return

}

// Main function
func main(){
	var list [10]int
	var find int

  fmt.Println("Enter an element : ")

	for i := 0; i < 10; i++ {
		fmt.Scan(&list[i])
	}

	fmt.Println("Find an element : ")
	fmt.Scan(&find)
	linearSearch(list, find)

}