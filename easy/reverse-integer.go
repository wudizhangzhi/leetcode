package main

import (
	"fmt"
	"math"
)

// -231 <= x <= 231 - 1
func reverse(x int) int {
	rev := 0
	for x != 0 {
		pop := x % 10
		x /= 10
		// fmt.Println(rev, pop, x)
		rev = rev*10 + pop
		if rev > int(math.Pow(2, 31))-1 {
			return 0
		} else if rev < int(-math.Pow(2, 31)) {
			return 0
		}

	}
	return rev
}

func main() {
	x := -2147483412
	ret := reverse(x)
	fmt.Println(ret)
}
