"""
@Time: 2025/2/18 10:35
@Author: yanzx
@Desc:
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        先按 子列表的第一个数排序，在对比 每一个子数组的最后一个和下一个子数组的第一个
        :param intervals:
        :return:
        """

        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] > intervals[i][0]:
                res[-1][1] = max(res[i - 1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res


# 示例使用
intervals = [[1, 4], [4, 5]]
sol = Solution()
print(sol.merge(intervals))  # 使用实例化的对象来调用方法
