package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

/*
https://leetcode.com/problems/longest-substring-without-repeating-characters/

a b c a b c b b
start   repeatAt

if repeat:
	if repeatIdx + 1 >= start:
	   res = max(res, i - start)
	   start = repeatIdx + 1

*/
func lengthOfLongestSubstring(s string) int {
	length := len(s)
	if length <= 1 {
		return length
	}
	res := 0
	start := 0
	memo := map[rune]int{}
	for i, r := range s { // 遍历
		if repAt, ok := memo[r]; ok { // 存在
			if repAt+1 >= start { // 重复的字符位置在start之后才有意义
				res = max(res, i-start)
				start = repAt + 1 // 更新起始位置
			}
		}
		memo[r] = i
	}
	return max(res, length-start)
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb") == 3)
	fmt.Println(lengthOfLongestSubstring("bbbbb") == 1)
	fmt.Println(lengthOfLongestSubstring("pwwkew") == 3)
	fmt.Println(lengthOfLongestSubstring("") == 0)
	fmt.Println(lengthOfLongestSubstring(" ") == 1)
	fmt.Println(lengthOfLongestSubstring("au") == 2)
	fmt.Println(lengthOfLongestSubstring("aab") == 2)
	fmt.Println(lengthOfLongestSubstring("cdd") == 2)
	fmt.Println(lengthOfLongestSubstring("tmmzuxt") == 5)
	fmt.Println(lengthOfLongestSubstring("abba") == 2)
	fmt.Println(lengthOfLongestSubstring("aabaab!bb") == 3)
}
