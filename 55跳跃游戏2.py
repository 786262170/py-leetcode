# coding=utf8
"""
@Author: Changye Yang
@Date: 2024/1/18 10:37
汇总区间
"""
from typing import List

"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i] 
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

 

示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2
"""


class Solution:
    def jump(self, nums: List[int]) -> int:

        """尽可能到达最远位置（贪心），如果能到达某个位置，那一定能到达到它前面的所有位置。

        :param nums:
        :return:
        """
        max_i = 0
        next_i = 0
        k_num = 0
        for idx, val in enumerate(nums[:-1]):
            # 如果可以到达当前位置
            if max_i >= idx:
                # 更新可以当前位置可到达的最大位置
                max_i = max(max_i, idx + val)
                # 如果到达了当前位置，就更新跳跃的步树，同时更新下一次可以到达的位置
                if idx == next_i:
                    next_i = max_i
                    k_num += 1
        return k_num


def test_jump():
    prices = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
    res = Solution().jump(prices)
    assert res == 2


if __name__ == '__main__':
    test_jump()
