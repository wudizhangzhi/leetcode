package main

import "fmt"

/*
https://leetcode.com/problems/length-of-last-word/
*/
func lengthOfLastWord(s string) int {
	count := 0
	for i := len(s) - 1; i >= 0; i-- {
		if string(s[i]) != " " {
			count++
		} else if count > 0 {
			break
		}
	}
	return count
}

func main() {
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
	fmt.Println(lengthOfLastWord("a"))
}
