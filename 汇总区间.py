# coding=utf8
"""
@Author: Changye Yang
@Date: 2024/1/18 10:37
汇总区间
"""

"""
给定一个
无重复元素
的
有序
整数数组
nums 。

返回
恰好覆盖数组中所有数字
的
最小有序
区间范围列表 。也就是说，nums
的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于
nums
的数字
x 。

列表中的每个区间范围[a, b]
应该按如下格式输出：

"a->b" ，如果
a != b
"a" ，如果
a == b

示例
1：

输入：nums = [0, 1, 2, 4, 5, 7]
输出：["0->2", "4->5", "7"]
解释：区间范围是：
[0, 2] --> "0->2"
[4, 5] --> "4->5"
[7, 7] --> "7"
示例
2：

输入：nums = [0, 2, 3, 4, 6, 8, 9]
输出：["0", "2->4", "6", "8->9"]
解释：区间范围是：
[0, 0] --> "0"
[2, 4] --> "2->4"
[6, 6] --> "6"
[8, 9] --> "8->9"

提示：

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
nums
中的所有值都
互不相同
nums
按升序排列
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start = 0
        returns = []
        #
        nums.append(2**32)
        for i in range(1, len(nums)):
            if i < len(nums):
                if nums[i] != nums[i-1] + 1:
                    if start != i-1:
                        returns.append(f'{nums[start]}->{nums[i-1]}')
                    else:
                        returns.append(str(nums[start]))
                    start = i

        return returns


def test_summary_ranges():
    lst1 = Solution().summaryRanges([0, 1, 2, 4, 5, 7])
    assert lst1
    assert lst1[0] == "0->2"
    assert lst1[1] == "4->5"
    assert lst1[2] == "7"


test_summary_ranges()
