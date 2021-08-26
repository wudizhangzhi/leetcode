package main

import (
	"fmt"
	"math"
)

// https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3918/
// Given a non-negative integer c,
// decide whether there're two integers a and b such that a2 + b2 = c.
// Constraints:
// 0 <= c <= 231 - 1

func judgeSquareSum(c int) bool {
	count := 0
	var result bool
	defer func() {
		fmt.Printf("输入: %d, 循环次数: %d, 结果: %t \n", c, count, result)
	}()
	cf := float64(c)
	if c < 3 {
		return true
	}
	a := 0.0
	b := math.Floor(math.Sqrt(cf))
	for a <= b {
		count++
		val := a*a + b*b
		if val == cf {
			result = true
			return result
		} else if val > cf {
			b--
		} else {
			a++
		}
	}
	result = false
	return false
}

func main() {
	fmt.Println(judgeSquareSum(5) == true)
	fmt.Println(judgeSquareSum(3) == false)
	fmt.Println(judgeSquareSum(4) == true)
	fmt.Println(judgeSquareSum(2) == true)
	fmt.Println(judgeSquareSum(1) == true)
	fmt.Println(judgeSquareSum(0) == true)
	fmt.Println(judgeSquareSum(int(math.Pow(2, 31) - 1)))
}
