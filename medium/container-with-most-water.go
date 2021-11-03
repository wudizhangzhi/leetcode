package main

import (
	"fmt"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

/*
https://leetcode.com/problems/container-with-most-water/
某个vertical能产生的最大面积:找到比自己短的vertical的位置
*/
func maxArea(height []int) int {
	start := 0
	end := len(height) - 1
	startHeight := height[start]
	endHeight := height[end]
	area := min(startHeight, endHeight) * (end - start)
	var moveStart bool
	for start < end {
		if startHeight < endHeight {
			moveStart = true
		} else {
			moveStart = false
		}
		if moveStart {
			start++
			if height[start] > startHeight {
				startHeight = height[start]
				area = max(area, min(startHeight, endHeight)*(end-start))
			}
		} else {
			end--
			if height[end] > endHeight {
				endHeight = height[end]
				area = max(area, min(startHeight, endHeight)*(end-start))
			}
		}
	}
	return area
}

func main() {
	fmt.Println(maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}) == 49)
	fmt.Println(maxArea([]int{4, 3, 2, 1, 4}) == 16)
	fmt.Println(maxArea([]int{1, 2, 1}) == 2)
}
