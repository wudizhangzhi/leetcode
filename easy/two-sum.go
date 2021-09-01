package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {
	visited := map[int]int{}
	var result []int
	for i, num := range nums {
		difference := target - num
		if _, ok := visited[num]; ok {
			result = []int{visited[num], i}
			break
		} else {
			visited[difference] = i
		}
	}
	return result
}

func main() {
	nums := []int{3, 2, 4}
	target := 6
	fmt.Println(twoSum(nums, target))
}
