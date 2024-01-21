# coding=utf8
"""
@Author: Changye Yang
@Date: 2024/1/18 10:37
汇总区间
"""
from typing import List

"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2
 
"""


class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        for item in nums:
            if nums.count(item) > n:
                return item


def test_removeDuplicates():
    nums1 = [1, 2, 3, 4, 4, 4]
    k = Solution().removeDuplicates(nums1)
    assert nums1 == [1, 2, 3, 4]
    assert k == 4


test_removeDuplicates()
