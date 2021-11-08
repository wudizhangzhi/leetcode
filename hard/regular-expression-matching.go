package main

import "fmt"

func isMatch(s string, p string) bool {
	return false
}

func main() {
	fmt.Println(isMatch("aab", "c*a*b") == true)
	fmt.Println(isMatch("mississippi", "mis*is*p*.") == false)
}
