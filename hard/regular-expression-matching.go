package main

import "fmt"

/*
动态规划
dymanic programming
*/
func isMatch(s string, p string) bool {
	dp := make([][]bool, len(s)+1)
	for i := 0; i < len(s)+1; i++ {
		dp[i] = make([]bool, len(p)+1)
	}
	dp[len(s)][len(p)] = true
	for i := len(s); i > -1; i-- {
		for j := len(p) - 1; j > -1; j-- {
			match := i < len(s) && (string(p[j]) == "." || p[j] == s[i])
			if j+1 < len(p) && string(p[j+1]) == "*" {
				dp[i][j] = dp[i][j+2] || match && dp[i+1][j]
			} else {
				dp[i][j] = match && dp[i+1][j+1]
			}
		}
	}
	return dp[0][0]
}

func main() {
	fmt.Println(isMatch("aab", "c*a*b") == true)
	fmt.Println(isMatch("mississippi", "mis*is*p*.") == false)
}
