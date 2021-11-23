package main

import (
	"fmt"
	"time"
)

/*
创建10个goroutine,id分别是0,1,2,3...9
每个goroutine只能打印最后一位是自己id号的数字， 例如: 3号只能打印3, 13, 23, 33...
编写一个程序，依次打印1-10000
*/

var IsRunning = true

func print(gid int, m map[int]chan int) {
	curChan := m[gid]
	nextChan := m[(gid+1)%10]
	for IsRunning {
		select {
		case i, ok := <-curChan:
			if ok {
				fmt.Println(fmt.Sprintf("%d   goroutine id=%d", i, gid))
				i++
				if i > 10000 {
					IsRunning = false
				} else {
					nextChan <- i
				}
			}
		}
	}

}

func printInOrder() {

	memo := map[int]chan int{}
	for i := 0; i < 10; i++ {
		c := make(chan int, 1)
		memo[i] = c
	}
	fmt.Printf("%#+v\n", memo)

	for i := 0; i < 10; i++ {
		go print(i, memo)
	}
	firstChan := memo[0]
	firstChan <- 0
	for IsRunning {
		// time.Sleep(time.Millisecond)
	}
	defer func() {
		for k, c := range memo {
			fmt.Printf("关闭: %d\n", k)
			close(c)
		}
	}()
}

func main() {
	start := time.Now()
	printInOrder()
	fmt.Printf("用时: %s", time.Since(start))
}
