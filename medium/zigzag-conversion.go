package main

import "fmt"

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}
	length := len(s)
	result := ""
	var pos, dif, sum int
	col, row := 0, 0
	for len(result) != length {
		result += string(s[pos])
		if row == 0 || row == numRows-1 { // 首行、末行
			dif = (numRows - 1) * 2
		} else if col%2 == 0 { // 偶数列
			dif = (numRows - 1 - row) * 2
		} else { // 奇数列
			dif = row * 2
		}
		sum = pos + dif
		if sum/length > 0 {
			col = 0
			row++
			pos = row
			continue
		} else {
			col++
		}
		pos = sum % length
	}
	return result
}

func main() {
	fmt.Println(convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
	fmt.Println(convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
	fmt.Println(convert("A", 1) == "A")
	fmt.Println(convert("AB", 1) == "AB")
}
