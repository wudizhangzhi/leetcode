package main

import (
	"fmt"
	"sort"
)

func abs(a int) int {
	if a < 0 {
		a = -a
	}
	return a
}

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	result := nums[0] + nums[1] + nums[2]
	diff := abs(result - target)
	for i, a := range nums {
		if i > 0 && a == nums[i-1] {
			continue
		}
		l, r := i+1, len(nums)-1
		for l < r {
			sum := a + nums[l] + nums[r]
			tmpDif := sum - target
			if tmpDif == 0 {
				return target
			} else if tmpDif > 0 {
				r--
			} else {
				l++
			}
			if abs(tmpDif) < diff {
				result = sum
				diff = abs(tmpDif)
			}
		}
	}
	return result
}

func main() {
	fmt.Println(threeSumClosest([]int{-1, 2, 1, -4}, 1) == 2)
	fmt.Println(threeSumClosest([]int{0, 0, 0}, 1) == 0)
}
