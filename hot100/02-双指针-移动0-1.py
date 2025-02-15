"""
@Time: 2025/2/15 21:26
@Author: yanzx
@Desc:
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
"""
nums = [0, 1, 0, 3, 12]
nums = [1, 0, 1, 0]
nums = [0, 0]
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        :param nums:
        :return:
        """

        left = 0
        for i in range(1, len(nums)):
            if nums[left] != 0 and left == 0 and nums[i] == 0:
                left = i
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1#注意不是left = i,这样很容易跳过中间的0
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]

    res = s.moveZeroes(nums)
    print(res)
