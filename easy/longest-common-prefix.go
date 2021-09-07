package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	flag := strs[0]
	idx := 1
	for flag != "" && idx < len(strs) {
		_flag := ""
		for i, s := range flag {
			if i < len(strs[idx]) && string(strs[idx][i]) == string(s) {
				_flag += string(s)
			} else {
				break
			}
		}
		flag = _flag
		idx++
	}
	return flag
}

func main() {
	strs := []string{"flower", "flow", "flight"}
	fmt.Println(longestCommonPrefix(strs))
}
