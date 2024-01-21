# coding=utf8
"""
@Author: Changye Yang
@Date: 2024/1/18 10:37
汇总区间
"""
from typing import List

"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

说明：

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        双指针
        """
        n = len(nums)
        if n < 2:
            return n
        slow = 2
        fast = 2
        while fast < n:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        # 更新num列表长度
        nums = nums[:slow]
        return slow


def test_removeDuplicates():
    nums1 = [1, 2, 2, 2, 3, 3, 4, 4, 4]
    so = Solution()
    k = so.removeDuplicates(nums1)
    print(nums1, k)
    assert nums1 == [1, 2, 2, 3, 3, 4, 4]
    assert k == 4


test_removeDuplicates()
