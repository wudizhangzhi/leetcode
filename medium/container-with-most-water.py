# coding=utf8

"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
from typing import List


class Solution(object):
    def maxArea(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxAero = 0
        while i < j:
            minHeight = min(height[i], height[j])
            maxAero = max(maxAero, (j - i) * minHeight)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxAero
