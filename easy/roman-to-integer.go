package main

import "fmt"

// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000
// I can be placed before V (5) and X (10) to make 4 and 9.
// X can be placed before L (50) and C (100) to make 40 and 90.
// C can be placed before D (500) and M (1000) to make 400 and 900.
func romanToInt(s string) int {
	m := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	i := 0
	maxLen := len(s)
	val := 0
	for i < maxLen {
		if i < len(s)-1 && m[s[i:i+1]] < m[s[i+1:i+2]] {
			val += m[s[i+1:i+2]] - m[s[i:i+1]]
			i += 2
		} else {
			val += m[s[i:i+1]]
			i++
		}

	}
	return val
}

func main() {
	s := "LVIII"
	fmt.Println(romanToInt(s))
	fmt.Println(romanToInt("IV"))
	fmt.Println(romanToInt("MCMXCIV"))
}
