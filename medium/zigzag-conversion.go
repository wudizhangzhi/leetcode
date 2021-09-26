package main

import "fmt"

func convert(s string, numRows int) string {
	length := len(s)
	result := ""
	pos := 0
	row := 0
	for len(result) != length {
		result += string(s[pos])
		sum := pos + numRows + numRows - 2
		if sum >= length {
			row++
		}
		pos = (sum - row) % length
		fmt.Println(pos, row, result)
	}
	fmt.Println(result)
	return result
}

func main() {
	fmt.Println(convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
	fmt.Println(convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
	fmt.Println(convert("A", 1) == "A")
}
