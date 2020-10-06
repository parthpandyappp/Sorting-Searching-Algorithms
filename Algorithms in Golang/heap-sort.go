package main

import "fmt"

func heapify(arr []int, idx int, size int) {
	l := 2*idx + 1 // left = 2*i + 1
	r := 2*idx + 2 // right = 2*i + 2

	var largest int
	if l <= size && arr[l] > arr[idx] {
		largest = l
	} else {
		largest = idx
	}

	if r <= size && arr[r] > arr[largest] {
		largest = r
	}

	if largest != idx {
		t := arr[idx]
		arr[idx] = arr[largest]
		arr[largest] = t
		heapify(arr, largest, size)
	}

}

// HeapSort :the array is divided into sorted and an unsorted parts, and then it iterates to
// shrink the unsorted region by extracting the largest element and moving that to the sorted part
func HeapSort(arr []int) {

	size := len(arr)     //heap size
	mid := int(size / 2) //middle

	for i := mid; i >= 0; i-- {
		heapify(arr, i, size-1)
	}

	F := size - 1
	for j := F; j >= 0; j-- {
		t := arr[0]
		arr[0] = arr[j]
		arr[j] = t
		F = F - 1
		heapify(arr, 0, F)
	}

}

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
	HeapSort(slice)
	fmt.Println("\nSorted array is: \n", slice, "\n")

}
