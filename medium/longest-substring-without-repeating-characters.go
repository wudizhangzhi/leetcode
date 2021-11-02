package main

import "fmt"

/*
https://leetcode.com/problems/longest-substring-without-repeating-characters/
*/
func lengthOfLongestSubstring(s string) int {
	return 0
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb") == 3)
	fmt.Println(lengthOfLongestSubstring("bbbbb") == 1)
	fmt.Println(lengthOfLongestSubstring("pwwkew") == 3)
	fmt.Println(lengthOfLongestSubstring("") == 0)
}
