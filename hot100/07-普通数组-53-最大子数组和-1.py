"""
@Time: 2025/2/17 19:33
@Author: yanzx
@Desc:
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        当前取最大的 保证全局也是最大的
        :param nums:
        :return:
        """
        res = tmp = nums[0]
        n = len(nums)
        for i in range(1,n):
            tmp = max(nums[i], nums[i]+tmp)
            res = max(res,tmp)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    res = s.maxSubArray(nums)
    print(res)
