package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func largestRectangleArea(heights []int) int {
	length := len(heights)
	left := make([]int, length) // 当前i的柱子的高度，左边能延伸到最远的地方(heights[i]< heights[left[i]], 存储的下标最左边的一个值)
	right := make([]int, length)
	stack := []int{}
	for i := 0; i < length; i++ {
		for len(stack) > 0 && heights[stack[len(stack)-1]] >= heights[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			left[i] = -1
		} else {
			left[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	stack = []int{}
	for i := length - 1; i > 0; i-- {
		for len(stack) > 0 && heights[stack[len(stack)-1]] >= heights[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			right[i] = -1
		} else {
			right[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	ans := 0
	for i := 0; i < length-1; i++ {
		ans = max(ans, (right[i]-left[i]-1)*heights[i])
	}
	fmt.Println(ans)
	return ans
}

func main() {
	fmt.Println(largestRectangleArea([]int{2, 1, 5, 6, 2, 3}) == 10)
}
