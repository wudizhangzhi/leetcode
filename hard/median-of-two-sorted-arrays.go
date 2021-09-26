package main

import "fmt"

/*
思路：
	寻找两个有序array中第k个
	每次两个array取一半
1.两个array一分为2, 长度分别为m1, m2
2.如果 k <= m1 + m2: 则第k个在左侧，
	两个array中较大的，截取左边(例如：nums2[:m2])
3.如果 k >  m1 + m2: 则第k个在右侧,
	两个array中较小的，截取右边(例如：nums1[m1:]), k减去array左边的长度, k=k-(m1+1)
4.循环，直到 两个array长度=0或者k=0
*/
func findKth(nums1 []int, nums2 []int, k int) float64 {
	for {
		l1, l2 := len(nums1), len(nums2)
		m1, m2 := l1/2, l2/2
		if l1 == 0 {
			return float64(nums2[k])
		} else if l2 == 0 {
			return float64(nums1[k])
		} else if k == 0 {
			if n1, n2 := nums1[0], nums2[0]; n1 < n2 {
				return float64(n1)
			} else {
				return float64(n2)
			}
		}

		if k <= m1+m2 {
			if nums1[m1] <= nums2[m2] {
				nums2 = nums2[:m2]
			} else {
				nums1 = nums1[:m1]
			}
		} else {
			if nums1[m1] < nums2[m2] {
				nums1 = nums1[m1+1:]
				k -= m1 + 1
			} else {
				nums2 = nums2[m2+1:]
				k -= m2 + 1
			}
		}
	}
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	if l := len(nums1) + len(nums2); l%2 == 0 {
		return (findKth(nums1, nums2, l/2-1) + findKth(nums1, nums2, l/2)) / 2.0
	} else {
		return findKth(nums1, nums2, l/2)
	}
}

func findMedianSortedArrays2(nums1 []int, nums2 []int) float64 {
	l1, l2 := len(nums1), len(nums2)
	if l1 > l2 {
		return findMedianSortedArrays2(nums2, nums1)
	}
	var i, j, mLeft, mRight int

	imin, imax, half := 0, l1, (l1+l2+1)/2
	for imin <= imax {
		i = (imin + imax) / 2
		j = half - i
		fmt.Println(i, j, nums1, nums2)
		if i > 0 && nums1[i-1] > nums2[j] {
			imax = i - 1
		} else if i < l1 && nums2[j-1] > nums1[i] {
			imin = i + 1
		} else {
			break
		}
	}
	if i == 0 {
		mLeft = nums2[j-1]
	} else if j == 0 {
		mLeft = nums1[i-1]
	} else if n1, n2 := nums1[i-1], nums2[j-1]; n1 < n2 {
		mLeft = n2
	} else {
		mLeft = n1
	}
	if (l1+l2)%2 == 1 {
		return float64(mLeft)
	}

	if i == l1 {
		mRight = nums2[j]
	} else if j == l2 {
		mRight = nums1[i]
	} else if n1, n2 := nums1[i], nums2[j]; n1 < n2 {
		mRight = n1
	} else {
		mRight = n2
	}
	return float64(mLeft+mRight) / 2.0

}

func main() {
	// 1,2,3,4,5,6,7
	// 1,2,3,4  5,6,7
	//  A > B
	//  A<-  B->
	// A[i-1] <= B[j]
	// A[i] >= B[j-1]
	// fmt.Println(findMedianSortedArrays([]int{1, 3}, []int{2}) == 2.0)
	// fmt.Println(findMedianSortedArrays([]int{1, 2}, []int{3, 4}) == 2.5)
	// fmt.Println(findMedianSortedArrays([]int{1}, []int{}) == 1)

	fmt.Println(findMedianSortedArrays2([]int{1, 3}, []int{2}) == 2.0)
	fmt.Println(findMedianSortedArrays2([]int{1, 2}, []int{3, 4}) == 2.5)
	fmt.Println(findMedianSortedArrays2([]int{1}, []int{}) == 1)
	fmt.Println(findMedianSortedArrays2([]int{0, 0}, []int{0, 0}) == 0)
}
