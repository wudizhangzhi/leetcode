package main

/*
创建10个goroutine,id分别是0,1,2,3...9
每个goroutine只能打印最后一位是自己id号的数字， 例如: 3号只能打印3, 13, 23, 33...
编写一个程序，依次打印1-10000
*/
type notifyChan chan int

func print(gid int, c notifyChan, s chan ) {
	for {
		select {
		case i<-c:
			fmt.Println(i)
		case <-s:
			break
		}
	}
	
}

func printInOrder() {
	memo := [int]notifyChan map{}
	for i:=0;i<9;i++{
		memo[i] = make(notifyChan, 1)
	}

}




func main() {
	printInOrder()
}