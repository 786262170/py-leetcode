# coding=utf8
"""
@Author: Changye Yang
@Date: 2024/1/18 10:37
汇总区间
"""
from typing import List

"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
"""


class Solution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 海象表达式，如果k对列表数量取余存在则执行
        if k := (k % len(nums)):
            # 交换前后k位置
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
        print(nums)


def test_rotate():
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums1, 3)
    assert nums1 == [5, 6, 7, 1, 2, 3, 4]


test_rotate()
