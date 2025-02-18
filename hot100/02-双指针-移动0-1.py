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
        左指针左边均为非零数；

        右指针左边直到左指针处均为零。
        :param nums:
        :return:
        """
        left = right = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]

    res = s.moveZeroes(nums)
    print(res)
