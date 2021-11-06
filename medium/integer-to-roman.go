package main

import "fmt"

/*
https://leetcode.com/problems/integer-to-roman/
*/
func intToRoman(num int) string {
	m := map[int]string{
		1:    "I",
		4:    "IV",
		5:    "V",
		9:    "IX",
		10:   "X",
		40:   "XL",
		50:   "L",
		90:   "XC",
		100:  "C",
		400:  "CD",
		500:  "D",
		900:  "CM",
		1000: "M",
	}
	result := ""
	for _, i := range []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1} {
		for num/i > 0 {
			num -= i
			result += m[i]
		}
	}
	return result
}

func main() {
	fmt.Println(intToRoman(3) == "III")
	fmt.Println(intToRoman(58) == "LVIII")
	fmt.Println(intToRoman(1994) == "MCMXCIV")
}
