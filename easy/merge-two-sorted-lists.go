package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	resultNode := &ListNode{}
	currentNode := resultNode
	for l1 != nil || l2 != nil {
		var isLeft bool
		if l1 == nil {
			isLeft = false
		} else if l2 == nil {
			isLeft = true
		} else if l1.Val < l2.Val {
			isLeft = true
		} else {
			isLeft = false
		}

		if isLeft {
			currentNode.Next = &ListNode{
				Val: l1.Val,
			}
			l1 = l1.Next
		} else {
			currentNode.Next = &ListNode{
				Val: l2.Val,
			}
			l2 = l2.Next
		}
		currentNode = currentNode.Next
	}
	return resultNode.Next
}

func main() {
	l1 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 4,
			},
		},
	}
	l2 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 3,
			Next: &ListNode{
				Val: 4,
			},
		},
	}
	l := mergeTwoLists(l1, l2)
	for l != nil {
		fmt.Println(l.Val)
		l = l.Next
	}
	fmt.Println("==================")
	// var l1 = &ListNode{}
	l2 = &ListNode{
		Val: 0,
	}
	l = mergeTwoLists(nil, l2)
	for l != nil {
		fmt.Println(l.Val)
		l = l.Next
	}

}
