package main

import (
	"fmt"
	"math"
	"strconv"
)

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	} else if x == 0 {
		return true
	}

	bit := len(strconv.Itoa(x)) // 位数
	for i := 0; i < bit/2; i++ {
		left := x / int(math.Pow(10, float64(bit-i-1))) % 10
		right := x / int(math.Pow(10, float64(i))) % 10
		// fmt.Println(i, left, right)
		if left != right {
			return false
		}
	}
	return true
}

func main() {
	x := 121
	fmt.Println(isPalindrome(x))
	fmt.Println(isPalindrome(int(math.Pow(2, 31) - 1)))
}
