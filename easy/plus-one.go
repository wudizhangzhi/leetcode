package main

import "fmt"

func plusOne(digits []int) []int {
	length := len(digits)
	idx := length - 1
	addition := 1
	for addition > 0 && idx >= 0 {
		tmp := digits[idx] + addition
		addition = tmp / 10
		digits[idx] = tmp % 10
		idx--
	}
	if idx < 0 && addition > 0 {
		tmpDigits := []int{addition}
		tmpDigits = append(tmpDigits, digits...)
		digits = tmpDigits
	}
	return digits
}

func main() {
	fmt.Println(plusOne([]int{1, 2, 3}))
	fmt.Println(plusOne([]int{4, 3, 2, 1}))
	fmt.Println(plusOne([]int{9}))
}
