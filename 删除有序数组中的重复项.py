# coding=utf8
"""
@Author: Changye Yang
@Date: 2024/1/18 10:37
汇总区间
"""
from typing import List

"""
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
判题标准:

系统会用下面的代码来测试你的题解:

int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有断言都通过，那么您的题解将被 通过。
"""


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pre = nums[0]
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != pre:
                nums[k] = nums[i]
                k += 1
                pre = nums[i]

        nums = nums[:k]
        return k


def test_removeDuplicates():
    nums1 = [1, 2, 3, 4, 4, 4]
    k = Solution().removeDuplicates(nums1)
    assert nums1 == [1, 2, 3, 4]
    assert k == 4


test_removeDuplicates()
