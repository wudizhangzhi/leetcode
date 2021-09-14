package main

import "fmt"

// https://leetcode.com/problems/remove-element/
func removeElement(nums []int, val int) int {
	i := 0
	for j := 0; j < len(nums); j++ {
		if nums[j] != val {
			nums[i], nums[j] = nums[j], nums[i]
			i++
		}
	}
	fmt.Println(nums)
	return i
}

func main() {
	fmt.Println(removeElement([]int{3, 2, 2, 3}, 3))
}
