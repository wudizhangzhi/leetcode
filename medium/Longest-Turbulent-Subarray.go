package main

import "fmt"

func max(i, j int) int {
	if i > j {
		return i
	}
	return j
}

func cmp(a, b int) int {
	if a < b {
		return -1
	} else if a == b {
		return 0
	} else {
		return 1
	}
}

/*
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3976/
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of
elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is
said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
*/
func maxTurbulenceSize(arr []int) int {
	N := len(arr)
	anchor := 0 // 锚点
	ans := 1    // 起码是1
	for i := 1; i < N; i++ {
		c := cmp(arr[i-1], arr[i])
		if c == 0 {
			anchor = i
		} else if i == N-1 || c*cmp(arr[i], arr[i+1]) != -1 { // 最后一个 或者 两边趋势不对（应该一增一减）
			ans = max(ans, i-anchor+1) // 最大值是当前到锚点的个数
			anchor = i                 // 重订锚点
		}
	}
	return ans
}

func main() {
	fmt.Println(maxTurbulenceSize([]int{9, 4, 2, 10, 7, 8, 8, 1, 9}) == 5)
	fmt.Println(maxTurbulenceSize([]int{4, 8, 12, 16}) == 2)
	fmt.Println(maxTurbulenceSize([]int{100}) == 1)
	fmt.Println(maxTurbulenceSize([]int{0, 8, 45, 88, 48, 68, 28, 55, 17, 24}) == 8)
	fmt.Println(maxTurbulenceSize([]int{8, 8, 9, 10, 6, 8, 2, 4, 2, 2, 10, 6, 6, 10, 10, 2, 3, 5, 1, 2, 10, 4, 2, 0, 9, 4, 9, 3, 0, 6, 3, 2, 3, 10, 10, 6, 4, 6, 4, 4, 2, 5, 1, 4, 1, 1, 9, 8, 9, 5, 3, 5, 5, 4, 5, 5, 6, 5, 3, 3, 7, 2, 0, 10, 9, 7, 7, 3, 5, 1, 0, 9, 6, 3, 1, 3, 4, 4, 3, 6, 3, 2, 1, 4, 10, 2, 3, 4, 4, 3, 6, 7, 6, 2, 1, 7, 0, 6, 8, 10}) == 7)
}
