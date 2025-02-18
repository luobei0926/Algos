"""
@Time: 2025/2/15 21:14
@Author: yanzx
@Desc:
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
示例 1：

输入：nums = [-1,0,1,2,-1,-4]
nums = [-4,-1,-1,0,1,2]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        先固定一个数 再从右边的数里面通过双指针进行操作
        :param nums:
        :return:
        """
        res = []
        nums = sorted(nums)
        l = len(nums)
        for i in range(l):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, l - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = s.threeSum(nums)
    print(res)  # 输出：[[-1, -1, 2], [-1, 0, 1]]
