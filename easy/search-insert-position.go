package main

import "fmt"

/*
 https://leetcode.com/problems/search-insert-position/
 Given a sorted array of distinct integers and a target value,
 return the index if the target is found. If not, return the index
 where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
*/
func searchInsert(nums []int, target int) int {
	s, e := 0, len(nums)-1
	for s <= e {
		mid := (s + e) / 2
		if target == nums[mid] {
			return mid
		} else if target < nums[mid] {
			e = mid - 1
		} else {
			s = mid + 1
		}
	}
	return e + 1
}

func main() {
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 5) == 2)
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 2) == 1)
	fmt.Println(searchInsert([]int{1}, 0) == 0)
}
