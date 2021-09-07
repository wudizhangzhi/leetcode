package main

import (
	"fmt"
	"strings"
)

// https://leetcode.com/problems/valid-parentheses/
func isValid(s string) bool {
	m := map[string]string{
		"(": ")",
		"[": "]",
		"{": "}",
	}
	leftArray := []string{}
	for _, x := range s {
		xs := string(x)
		if strings.Index("([{", xs) > -1 {
			leftArray = append(leftArray, xs)
		} else if strings.Index(")]}", xs) > -1 {
			if len(leftArray) == 0 {
				return false
			}
			lastLeft := leftArray[len(leftArray)-1]
			if m[lastLeft] != xs {
				return false
			}
			leftArray = leftArray[0 : len(leftArray)-1]
		} else {
			return false
		}
	}
	if len(leftArray) > 0 {
		return false
	}
	return true
}

func main() {
	s := "()[]{}"
	fmt.Println(isValid(s))
	fmt.Println(isValid("([)]{}"))
	fmt.Println(isValid(")("))
}
