"""
@Time: 2025/2/17 14:10
@Author: yanzx
@Desc:
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
"""
from typing import List
from collections import defaultdict

class Solution:
    def hanshu(self, nums: list[int], k: int) -> int:
        """
        这个题目难在得到sum之后  怎么去加个数 后面的思路值得好好学习
        :param nums:
        :param k:
        :return:
        """
        res = 0
        n = len(nums)
        s = [0] * (n + 1)

        for i in range(1, n+1):
            s[i] = s[i - 1] + nums[i-1]
        print(s)
        d = defaultdict(int)
        for si in s:
            res += d[si - k]
            d[si] += 1
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1]
    k = 2
    print(s.hanshu(nums, k))
