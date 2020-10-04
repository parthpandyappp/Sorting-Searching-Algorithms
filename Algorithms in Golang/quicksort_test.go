package main

import (
	"math/rand"
	"testing"
)

func isIncreasing(arr []int) bool {
	for i := 1; i < len(arr); i++ {
		if arr[i] < arr[i-1] {
			return false
		}
	}
	return true
}

func TestQuickSort(T *testing.T) {
	for i := 0; i < 1000; i++ {
		length := rand.Intn(10000)
		arr := rand.Perm(length)
		QuickSort(arr)
		if !isIncreasing(arr) {
			T.Fatal("Test failed")
		}
	}
}
