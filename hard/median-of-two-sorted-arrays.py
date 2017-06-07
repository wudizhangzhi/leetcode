#coding=utf8

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time
 complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''


'''
        left_part        |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

条件:
1. A[i-1] <= B[j] and B[j-1] <= A[i]
2. i + j = (m + n)/2
令 i = 0 ~ min(m, n)
则 j = (m + n)/2 - i
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1
        B = nums2
        m, n = len(A), len(B)
        if m > n:
            B , A, n, m = A, B, m, n
        if n<=0:
            raise ValueError
        imin, imax, half_len = 0, m, (m + n)/2
        while imin <= imax:
            i = (imin + imax)/2
            j = half_len - i
            if i > 0 and A[i-1] > B[j]: # i too big ,decrease i
                imax -= 1
                print('imax --: %s' % imax)
            elif i < m and B[j-1] > A[i]: # i too small, increase i
                imin += 1
                print('imin ++: %s' % imin)
            else: # 符合条件
                if i == 0:
                    max_left = B[j-1]
                elif j == 0:
                    max_left = A[i-1]
                else:
                    max_left = max(A[i-1], B[j-1])
                if (m+n)%2 == 1: # length of (nums1, nums2) is odd
                    return max_left
                # length of (nums1, nums2) is even
                if i == m:
                    min_right = B[j]
                elif j == n:
                    min_right = A[i]
                else:
                    min_right = min(A[i], B[j])
                return (max_left + min_right) / 2.0






if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4, 5, 6, 7, 8]

    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(result)
