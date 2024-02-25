# coding=utf8
"""
@Author: Changye Yang
@Date: 2024/1/18 10:37
汇总区间
"""
from typing import List

"""
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        """尽可能到达最远位置（贪心），如果能到达某个位置，那一定能到达到它前面的所有位置。

        :param nums:
        :return:
        """
        max_i = 0
        for idx, val in enumerate(nums[:-1]):
            if idx <= max_i < idx + val:
                max_i = idx + val
        return max_i >= len(nums)-1


def test_canJump():
    prices = [2, 0, 0]
    res = Solution().canJump(prices)
    assert res is True


if __name__ == '__main__':
    test_canJump()
