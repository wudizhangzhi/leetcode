package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

/*
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
*/
func minStartValue(nums []int) int {
	minVal := 0
	sum := 0
	for _, num := range nums {
		sum += num
		minVal = min(minVal, sum)
	}
	return -minVal + 1
}

func main() {
	fmt.Println(minStartValue([]int{-3, 2, -3, 4, 2}) == 5)
	fmt.Println(minStartValue([]int{1, 2}) == 1)
	fmt.Println(minStartValue([]int{1, -2, -3}) == 5)
}
