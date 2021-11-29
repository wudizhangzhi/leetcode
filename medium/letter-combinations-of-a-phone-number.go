package main

import "fmt"

var letterMap = map[string][]string{
	"2": {"a", "b", "c"},
	"3": {"d", "e", "f"},
	"4": {"g", "h", "i"},
	"5": {"j", "k", "l"},
	"6": {"m", "n", "o"},
	"7": {"p", "q", "r", "s"},
	"8": {"t", "u", "v"},
	"9": {"w", "x", "y", "z"},
}

func letterCombinations(digits string) []string {
	ret := []string{}
	var backtrack func(int, string)
	backtrack = func(i int, curStr string) {
		if len(curStr) == len(digits) {
			ret = append(ret, curStr)
			return
		}
		for _, c := range letterMap[string(digits[i])] {
			backtrack(i+1, curStr+c)
		}
	}
	if len(digits) > 0 {
		backtrack(0, "")
	}
	return ret
}

func main() {
	fmt.Println(letterCombinations("23"))
	fmt.Println(letterCombinations(""))
	fmt.Println(letterCombinations("2"))
}
