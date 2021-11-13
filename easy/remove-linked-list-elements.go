package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
	if head == nil || head.Val == 0 {
		return head
	}
	ret := &ListNode{
		Next: head,
	}
	curHead := ret
	for curHead != nil && curHead.Next != nil {
		if curHead.Next.Val == val {
			curHead.Next = curHead.Next.Next
		} else {
			curHead = curHead.Next
		}
		// fmt.Printf("%#v\n", curHead)
	}
	return ret.Next
}

func main() {
	head := ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 6,
				Next: &ListNode{
					Val: 3,
					Next: &ListNode{
						Val: 4,
						Next: &ListNode{
							Val: 5,
							Next: &ListNode{
								Val: 6,
							},
						},
					},
				},
			},
		},
	}
	// fmt.Println(removeElements(&head, 6))
	// head = ListNode{}
	// fmt.Println(removeElements(&head, 1))
	// fmt.Println(removeElements(nil, 1))
	head = ListNode{
		Val: 7,
		Next: &ListNode{
			Val: 7,
			Next: &ListNode{
				Val: 7,
				Next: &ListNode{
					Val: 7,
				},
			},
		},
	}
	fmt.Println(removeElements(&head, 7))
}
