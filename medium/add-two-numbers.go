package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
https://leetcode.com/problems/add-two-numbers/
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
*/
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	result := &ListNode{}
	current := result

	higher := 0
	for l1 != nil || l2 != nil || higher > 0 {
		a, b := 0, 0
		if l1 != nil {
			a = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			b = l2.Val
			l2 = l2.Next
		}
		sum := a + b + higher
		current.Next = &ListNode{
			Val: sum % 10,
		}
		higher = sum / 10
		current = current.Next
	}
	return result.Next
}

func listToListNode(l []int) *ListNode {
	ln := &ListNode{}
	var current *ListNode = ln
	for _, i := range l {
		current.Next = &ListNode{
			Val: i,
		}
		current = current.Next
	}
	return ln.Next
}

func printNode(l *ListNode) []int {
	a := []int{}
	for l != nil {
		a = append(a, l.Val)
		l = l.Next
	}
	return a
}

func main() {
	// l1 := ListNode{
	// 	Val: 2,
	// 	Next: &ListNode{
	// 		Val: 4,
	// 		Next: &ListNode{
	// 			Val: 3,
	// 		},
	// 	},
	// }
	// l2 := ListNode{
	// 	Val: 5,
	// 	Next: &ListNode{
	// 		Val: 6,
	// 		Next: &ListNode{
	// 			Val: 4,
	// 		},
	// 	},
	// }
	// fmt.Println(addTwoNumbers(&l1, &l2))

	fmt.Println(printNode(addTwoNumbers(listToListNode([]int{9, 9, 9, 9, 9, 9, 9}), listToListNode([]int{9, 9, 9, 9}))))
	// fmt.Println(printNode(addTwoNumbers(listToListNode([]int{0}), listToListNode([]int{0}))))

}
