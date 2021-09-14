package main

import "fmt"

// https://leetcode.com/problems/remove-duplicates-from-sorted-array/
// Input: nums = [0,0,1,1,1,2,2,3,3,4]
// [0,1,_,1,1,2,2,3,3,4]
// Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
func removeDuplicates(nums []int) int {
	l := 0
	for i := 0; i < len(nums); i++ {
		if i == 0 || nums[i] != nums[l-1] {
			nums[l] = nums[i]
			l++
		}
	}
	return l
}

func main() {
	nums := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	fmt.Println(removeDuplicates(nums))
	fmt.Println(removeDuplicates([]int{1, 1, 2}))

}
