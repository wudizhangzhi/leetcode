package main

import (
	"fmt"
)

func isPalindeome(l string) bool {
	start := 0
	end := len(l) - 1
	for start < end {
		if l[start] != l[end] {
			return false
		}
		start++
		end--
	}
	return true
}

func longestPalindrome(s string) string {
	length := len(s)
	if length <= 1 {
		return s
	}
	result := ""
	for i := 0; i < length; i++ { // 左边界
		for j := length; j > i; j-- { // 右边界
			if len(result) > j-i-1 {
				break
			}
			if isPalindeome(s[i:j]) {
				result = s[i:j]
				break
			}
		}
	}
	return result
}

func main() {
	fmt.Println(longestPalindrome("babad"))
	fmt.Println(longestPalindrome("cbbd"))
	fmt.Println(longestPalindrome("a"))
	fmt.Println(longestPalindrome("ac"))
	fmt.Println(longestPalindrome("bb"))
}
