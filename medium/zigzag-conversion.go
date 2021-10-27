package main

import "fmt"

func convert(s string, numRows int) string {
	length := len(s)
	result := ""
	var pos, dif, sum int
	col, row := 0, 0
	for len(result) != length {
		result += string(s[pos])
		if length-pos < numRows {
			row++ // 换行
			pos = row
			dif = 0
		} else if row == 0 || row == numRows-1 {
			dif = (numRows - 1) * 2
		} else if col%2 == 0 { // 偶数列
			dif = (numRows - 1 - row) * 2
		} else { // 奇数列
			dif = row * 2
		}
		fmt.Println(pos, dif, row, col, result)
		sum = pos + dif
		if sum/length > 0 {
			col = 0
		} else {
			col++
		}
		pos = sum % length
	}
	fmt.Println(result)
	return result
}

func main() {
	fmt.Println(convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
	fmt.Println(convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
	fmt.Println(convert("A", 1) == "A")
}
