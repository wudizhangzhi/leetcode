package main

import (
	"fmt"
	"strings"
)

/*
示例：numRows = 4
0P       6I        12N
1A    5L 7S    11I 13G
2Y 4A    8H 10R
3P       9I


每行的端点之间的距离是: 2*numRows - 2
除了第一行和最后一行：两个端点之间还有一个点，距前一个端点 2*nunRows-2 -row
*/
func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}
	var b strings.Builder
	length := len(s)
	cycle := 2*numRows - 2
	for i := 0; i < numRows; i++ { // 每行
		for j := 0; i+j < length; j += cycle { // 每个端点
			b.WriteByte(s[i+j])
			if i != 0 && i != numRows-1 && j+cycle-i < length { // 不是第一行，不是最后一行，且不超过长度
				b.WriteByte(s[j+cycle-i])
			}
		}
	}
	return b.String()
}

func main() {
	fmt.Println(convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
	fmt.Println(convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
	fmt.Println(convert("A", 1) == "A")
	fmt.Println(convert("AB", 1) == "AB")
}
