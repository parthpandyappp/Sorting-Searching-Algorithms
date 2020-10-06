package main

import (
	"fmt"
)

func QuickSort(arr []int) {
	if len(arr) == 0 {
		return
	}
	left := 0
	right := len(arr) - 1
	pivot := arr[right]
	right--

	for {
		for ; left <= right && arr[left] < pivot; left++ {
		}
		for ; right >= left && arr[right] > pivot; right-- {
		}
		if left >= right {
			break
		}
		arr[left], arr[right] = arr[right], arr[left]
		left++
		right--
	}
	arr[left], arr[len(arr)-1] = arr[len(arr)-1], arr[left]
	QuickSort(arr[:left])
	QuickSort(arr[left+1:])
}

func main() {
	var size int
	fmt.Println("Enter the size of an array : ")
	_, _ = fmt.Scan(&size)

	list := make([]int, 0)

	fmt.Println("Enter each element: ")
	for i := 0; i < size; i++ {
		var n int
		_, _ = fmt.Scan(&n)
		list = append(list, n)
	}
	QuickSort(list)
	fmt.Println(list)
}
